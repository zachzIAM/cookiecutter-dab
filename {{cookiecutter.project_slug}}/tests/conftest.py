"""
This conftest.py contains handy components that prepare SparkSession and other relevant objects.
"""

import logging
import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from sys import platform
from typing import Iterator
from unittest.mock import patch

import pytest
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

ISWINDOWS = platform == "win32" or (getattr(os, "_name", False) == "nt")


@dataclass
class FileInfoFixture:
    """
    This class mocks the DBUtils FileInfo object
    """

    path: str
    name: str
    size: int
    modificationTime: int


class DBUtilsFixture:
    """
    This class is used for mocking the behaviour of DBUtils inside tests.
    """

    def __init__(self):
        self.fs = self

    def cp(self, src: str, dest: str, recurse: bool = False):
        copy_func = shutil.copytree if recurse else shutil.copy
        copy_func(src, dest)

    def ls(self, path: str):
        _paths = Path(path).glob("*")
        _objects = [
            FileInfoFixture(str(p.absolute()), p.name, p.stat().st_size, int(p.stat().st_mtime))
            for p in _paths
        ]
        return _objects

    def mkdirs(self, path: str):
        Path(path).mkdir(parents=True, exist_ok=True)

    def mv(self, src: str, dest: str, recurse: bool = False):
        copy_func = shutil.copytree if recurse else shutil.copy
        shutil.move(src, dest, copy_function=copy_func)

    def put(self, path: str, content: str, overwrite: bool = False):
        _f = Path(path)

        if _f.exists() and not overwrite:
            raise FileExistsError("File already exists")

        _f.write_text(content, encoding="utf-8")

    def rm(self, path: str, recurse: bool = False):
        deletion_func = shutil.rmtree if recurse else os.remove
        deletion_func(path)


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """
    This fixture provides preconfigured SparkSession with Hive and Delta
    support with registered test data schemas and tables.
    After the test session, temporary warehouse directory is deleted.
    :return: SparkSession
    """
    logging.info("Configuring Spark session for testing environment")
    warehouse_dir = tempfile.TemporaryDirectory().name
    _builder = (
        SparkSession.builder.master("local[*]")
        .config("spark.hive.metastore.warehouse.dir", Path(warehouse_dir).as_uri())
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )

    # use win cert store to avoid SSL issues when downloading deltalake and other maven packages
    if ISWINDOWS:
        _builder.config(
            "spark.driver.extraJavaOptions",
            "-Djavax.net.ssl.trustStoreType=Windows-ROOT "
            "-Djavax.net.ssl.trustStore=C:\\Windows\\win.ini",
        )

    spark: SparkSession = configure_spark_with_delta_pip(_builder).getOrCreate()
    register_schemas(
        spark=spark,
        warehouse_dir=(Path(__file__).parent / "data").as_posix(),
    )

    logging.info("Spark session configured")
    yield spark
    logging.info("Shutting down Spark session")
    spark.stop()
    if Path(warehouse_dir).exists():
        shutil.rmtree(warehouse_dir)


def register_schemas(spark: SparkSession, warehouse_dir: str) -> None:
    warehouse_dir_ = Path(warehouse_dir)

    for schema in warehouse_dir_.iterdir():
        if schema.is_dir():
            _register_schema(spark=spark, schema_path=schema)


def _register_schema(spark: SparkSession, schema_path: Path):
    # create schema
    db = schema_path.name
    db_loc = schema_path.as_posix()
    sql = f"CREATE SCHEMA IF NOT EXISTS {db} LOCATION '{db_loc}'"
    spark.sql(sql)

    # register tables
    _init_db = spark.catalog.currentDatabase()
    spark.catalog.setCurrentDatabase("ext_qai")
    for table in schema_path.iterdir():
        if table.is_dir():
            spark.catalog.createTable(tableName=table.name, path=table.as_posix(), source="delta")
    spark.catalog.setCurrentDatabase(_init_db)


@pytest.fixture(scope="session", autouse=True)
def dbutils_fixture() -> Iterator[None]:
    """
    This fixture patches the `get_dbutils` function.
    Please note that patch is applied on a string name of the function.
    If you change the name or location of it, patching won't work.
    :return:
    """
    logging.info("Patching the DBUtils object")
    with patch("{{ cookiecutter.package_name }}.common.get_dbutils", lambda _: DBUtilsFixture()):
        yield
    logging.info("Test session finished, patching completed")


@pytest.fixture(scope="session")
def test_data_csv() -> str:
    pth = Path(__file__).parent / "data" / "test_data.csv"
    return pth.as_uri()
