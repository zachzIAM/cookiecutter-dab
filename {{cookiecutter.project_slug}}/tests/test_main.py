from {{ cookiecutter.package_name }} import main

def test_get_table(spark):
    # arrange
    expected_catalog = "samples"
    expected_schema = "nyctaxi"
    expected_table = "trips"

    # act
    result = main.get_table(catalog=expected_catalog, schema=expected_schema, table=expected_table)

    # assert
    assert result.count() > 0
    assert result.columns == ["column1", "column2", ...]  # Add expected column names here
    # Add more assertions as needed