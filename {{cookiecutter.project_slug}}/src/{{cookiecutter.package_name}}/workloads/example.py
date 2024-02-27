from {{ cookiecutter.package_name }}.common import Workload


class Example(Workload):
    def launch(self, *args, **kwargs):
        sdf = spark.sql("SELECT 'Hello World!' as greeting")
        sdf.show()
        return sdf


def entrypoint():
    example = Example()
    example.launch()