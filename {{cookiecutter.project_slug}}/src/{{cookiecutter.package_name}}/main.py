from pyspark.sql import SparkSession


def get_table(catalog: str = "samples", schema: str = "nyctaxi", table: str = "trips"):
    """
    Get the NYC taxi dataset from the samples.nyctaxi.trips table

    Args:
        catalog (str): The catalog of the table
        schema (str): The schema of the table
        table (str): The name of the table

    Returns:
        pyspark.sql.dataframe.DataFrame: The NYC taxi dataset
    """
    spark = SparkSession.builder.getOrCreate()
    return spark.read.table(f"{catalog}.{schema}.{table}")


def hello_world(name: str = "World"):
    """
    Return a greeting to the user

    Args:
        name (str): The name of the user

    Returns:
        pyspark.sql.dataframe.DataFrame: The greeting
    """
    spark = SparkSession.builder.getOrCreate()
    greeting = spark.sql(f"SELECT '{name}!' as greeting")
    return greeting


def main():
    """
    Main function

    Args:
        None

    Returns:
        None
    """
    get_taxis().show(5)
    hello_world().show()


if __name__ == "__main__":
    """
    Entry point for the application
    """
    main()
