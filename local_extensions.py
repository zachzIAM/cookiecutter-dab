from typing import Optional
from configparser import ConfigParser
from pathlib import Path
from jinja2.ext import Extension

# @simple_filter
# def default_databricks_host() -> Optional[str]:
#     config = ConfigParser()
#     config.read(find_databrickscfg())
#     return config.defaults().get("host")

class DatabricksHostExtension(Extension):
    def __init__(self, environment):
        super(DatabricksHostExtension, self).__init__(environment)
        environment.filters['default_databricks_host'] = default_databricks_host


def default_databricks_host() -> Optional[str]:
    config = ConfigParser()
    config.read(find_databrickscfg())
    return config.defaults().get("host")


def find_databrickscfg() -> str:
    path = Path().home() / ".databrickscfg"
    return path.as_posix()


