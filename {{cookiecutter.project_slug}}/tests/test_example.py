from {{ cookiecutter.package_name }}.workloads.example import Example as TestWorkload

def test_example(spark):
    # arrange
    test_workload = TestWorkload()

    # act
    result = test_workload.launch()

    # assert
    assert result.count() == 1
