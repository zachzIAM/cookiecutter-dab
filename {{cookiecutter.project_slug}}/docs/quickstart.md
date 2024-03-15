# Quickstart

Guide to get started with the project.

## Requirements

You need Python 3.12 and the following tools:

> **_NOTE:_** pipx is recommended to install the following tools.

Poetry

```console
$ pipx install poetry
```

Nox

```console
$ pipx install nox
```

nox-poetry

```console
$ pipx inject nox nox-poetry
```

[DataBricks CLI](https://docs.databricks.com/en/dev-tools/cli/install.html) via one of the methods

```console
### curl ###
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

### chocolatey ###
choco install databricks-cli

### winget ###
winget search databricks
winget install Databricks.DatabricksCLI
```

Update your .databricks.cfg file (usually located in `C:\Users\username\.databrickscfg`) with your databricks instance and token

```console
[AWS]
host = <AWS_DATABRICKS_HOST>
token = <AWS_DATABRICKS_TOKEN>
jobs-api-version = 2.0
insecure = True

[AZURE]
host = <AZURE_DATABRICKS_HOST>
token = <AZURE_DATABRICKS_TOKEN>
jobs-api-version = 2.0
insecure = True
```

Clone the repo via git

```console
$ git clone https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_slug}}
```

Install the package with development requirements:

```console
$ poetry install
```

## Running

Install the package with development requirements:

```console
$ poetry install
```

You can now run an interactive Python session, or the command-line interface:

```console
$ poetry run python
>>> import {{ cookiecutter.package_name }}
```

Deploy the Databricks asset bundle

```console
$ databricks bundle deploy
```

Run the Databricks asset bundle

```console
$ databricks bundle run
```

## Testing

Run the full test suite:

```console
$ nox
```

To run Nox in a single environment:

```console
$ nox --python=3.12
```

List the available Nox sessions:

```console
$ nox --list-sessions
```

You can also run a specific Nox session. For example, invoke the unit test suite like this:

```console
$ nox --session=tests
```

To run a specific Nox session in a specific environment:

```console
$ nox --session=pre-commit --python=3.12
```
