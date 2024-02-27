import re
import sys


def is_snake_case(value: str) -> bool:
    snake_case_pattern = "[a-z]+(?:_{1}[a-z]+)*[^-_]$"
    return bool(re.match(snake_case_pattern, value))

package_name = "{{ cookiecutter.package_name }}"

if not is_snake_case(package_name):
    print(f"ERROR: {package_name} is not a valid package name. Make sure you are using snakecase notation")

    sys.exit(1)
