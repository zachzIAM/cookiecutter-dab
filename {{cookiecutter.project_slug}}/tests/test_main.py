
import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType
from {{ cookiecutter.package_name }} import main.get_table, main.hello_world

@pytest.fixture(scope="session")
def spark_session():
    spark = SparkSession.builder.master("local").appName("PySparkTests").getOrCreate()
    yield spark
    spark.stop()

@pytest.fixture(scope="session")
def setup_sample_table(spark_session):
    # Mimic 'samples.nyctaxi.trips' table
    schema = StructType([StructField("trip_distance", StringType(), True)])
    data = [("1.2",), ("3.4",)]
    df = spark_session.createDataFrame(data, schema)
    df.createOrReplaceTempView("samples.nyctaxi.trips")

@pytest.fixture(scope="session")
def setup_hello_world_view(spark_session):
    # Temp view for testing hello_world function
    spark_session.sql("SELECT 'World!' as greeting").createOrReplaceTempView("hello_world")

def test_get_table(spark_session, setup_sample_table):
    df = get_table()
    assert df.columns == ["trip_distance"]
    assert df.count() == 2

def test_hello_world(spark_session, setup_hello_world_view):
    greeting_df = hello_world()
    expected_data = [("World!",)]
    actual_data = [row.asDict() for row in greeting_df.collect()]
    assert actual_data == [{'greeting': 'World!'}]
