# Contributor Guide

Thank you for your interest in improving this project.
This project welcomes contributions in the form of bug reports, feature requests, and pull requests.

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

[source code]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
[documentation]: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}
[issue tracker]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues

## Project Structure

This section outlines the logical structure of the project. It is intended to help developers understand the project and find their way around the codebase.

```bash
{{ cookiecutter.project_slug }}
│
├── .github                                 # GitHub related configuration files
│   ├── ISSUE_TEMPLATE                      # GitHub Issue Templates
│   │   ├── BUG_REPORT.md                   # Bug report issue template
│   │   ├── DOCUMENTATION.md                # Documentation issue template
│   │   ├── FEATURE_REQUEST.md              # Feature request issue template
│   ├── workflows                           # GitHub Actions
│   │   ├── constraints.txt                 # python package constraints for GitHub Actions
{% if cookiecutter.require_github_self_hosted_runner.lower() != 'n' %}
│   │   ├── documentation.yml               # Build sphinx docs and deploy to GitHub Pages workflow
{% endif %}
│   │   ├── labeler.yml                     # Labeler workflow
│   │   ├── release.yml                     # Release workflow to deploy to PyPI and TestPyPI
│   │   └── tests.yml                       # Tests workflow to run unit tests and code coverage
│   ├── dependabot.yml                      # Dependabot configuration
│   ├── labels.yml                          # Labels for GitHub Issues and Pull Requests
│   └── release-drafter.yml                 # Release Drafter configuration
│
{% if cookiecutter.require_github_self_hosted_runner.lower() != 'n' %}
├── docs                                    # Sphinx documentation
│   ├── Makefile                            # Makefile for building Sphinx documentation
│   ├── codeofconduct.md                    # Code of Conduct page for sphinx doc referencing ../CODE_OF_CONDUCT.md
│   ├── conf.py                             # Sphinx configuration
│   ├── contributing.md                     # Contributing page for sphinx doc referencing ../CONTRIBUTING.md
│   ├── index.md                            # Index page for sphinx doc referencing ../README.md
│   ├── license.md                          # License page for sphinx doc referencing ../LICENSE
│   ├── quickstart.md                       # Quickstart page for sphinx doc
│   └── requirements.txt                    # Requirements for building Sphinx documentation
{% endif %}
│
│── examples                                # Usecase examples of the project
│   └── example.ipynb                       # Example notebook using the python package
│
├── fixtures                                # Databricks asset bundle fixtures, reserved for fixtures like CSV files
│   └── .gitkeep                            # Placeholder file to keep the directory in the repo
│
├── resources                               # Databricks asset bundle resources, reserved for resources like SQL or YAML files used in the workflow
│   └── {{cookiecutter.package_name}}_job.yml # YAML file containing the ETL workflow
│
├── scratch                                 # Reserved for personal, exploratory notebooks. Usually excluded from the repo.
│   └── README.md                           # README for the scratch directory stating the above.
│
├── src                                     # Source code for python package
│   └── {{cookiecutter.package_name}}       # Python package
│   │   ├── __init__.py                     # Required for python package
│   │   ├── main.py                         # main module
│   │   └── py.typed                        # mypy type checking requirement
│   └── notebook.ipynb                      # Jupyter notebook used in the job
│
└── tests                                   # Unit tests
│   ├── __init__.py                         # Required for pytest to discover tests
│   ├── conftest.py                         # Contains handy testing components 
│   └── test_main.py                        # Tests for main.py
│
├── .darglint                               # Darglint configuration
├── .gitattributes                          # Git line ending handling - text files will have normalized (LF) line endings in the repo
├── .gitignore                              # Git ignore file - folders/files to ignore in the repo
├── .pre-commit-config.yaml                 # Pre-commit configuration
├── CONTRIBUTING.md                         # Contributing Guidelines
├── databricks.yml                          # Databricks asset bundle configuration
├── LICENSE                                 # License
├── Makefile                                # Makefile for automation of common tasks  
├── noxfile.py                              # Nox configuration for automation of testing, doc building, pre-commit, etc.
├── poetry.lock                             # Poetry lock file
├── pyproject.toml                          # Poetry configuration
└── README.md                               # Project README
```

## How to report a bug or request a feature

Report bugs or request features using the ready-made templates on the [Issue Tracker].
Please check existing issues before opening a new one.

## How to set up your development environment

You need Python 3.11+ and the following tools:

> **_NOTE:_** pipx is recommended to install the following tools.

[Poetry]

```console
$ pipx install poetry
```

[Nox]

```console
$ pipx install nox
```

[nox-poetry]

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
[AZURE]
host = <AZURE_DATABRICKS_HOST>
token = <AZURE_DATABRICKS_TOKEN>
jobs-api-version = 2.0
insecure = True
```

Clone the repo via git

```console
$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```

Install the package with development requirements:

```console
$ poetry install
```

You can now run an interactive Python session, or the command-line interface:

```console
$ poetry run python
>>> import {{ cookiecutter.project_slug }}
```

[poetry]: https://python-poetry.org/
[nox]: https://nox.thea.codes/
[nox-poetry]: https://nox-poetry.readthedocs.io/

## How to test the project

Run the full test suite:

```console
$ nox
```

You may experience errors running Nox if you do not have the available Python versions installed e.g. 3.11 & 3.12. To run Nox in a single environment:

```console
$ nox --python=3.11
```

List the available Nox sessions:

```console
$ nox --list-sessions
```

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

```console
$ nox --session=tests
```
Alternatively, you can run the nox sessions using _MAKE_ commands which will pick up your local python version. For example, to run the tests session, you can use the following command:

```console
$ make tests
```

Unit tests are located in the _tests_ directory, and are written using the [pytest] testing framework.

[pytest]: https://pytest.readthedocs.io/

## How to submit changes

### Step 1 - Check issue tracker

Ensure that the issue you are working on is not already open by searching the [issue tracker].

It is recommended to open an issue before starting work on anything. This will allow a chance to talk it over with the owners and validate your approach. Please create an issue if one does not already exist, ensuring that you follow the issue template.

### Step 2 - Create a branch

Create a new branch from main for your changes. Please ensure that your branch adheres to the naming convention `category/issue-reference/description`

**Category**

Pick one of the following categories for your branch:

- `feature` - for adding, refactoring or removing a feature
- `bugfix` - for fixing a bug
- `hotfix` - for changing code with a temporary solution and/or without following the usual process (usually because of an emergency)
- `test` - for experimenting outside of an issue/ticket

**Reference**

After the category, there should be a "/" followed by the reference of the issue/ticket you are working on. If there's no reference, just add no-ref.

**Description**

After the reference, there should be another "`/`" followed by a description which sums up the purpose of this specific branch. This description should be short and "kebab-cased".

By default, you can use the title of the issue/ticket you are working on. Just replace any special character by "`-`".

**Examples**

```bash
git branch feature/issue-42/create-new-button-component
git branch bugfix/issue-342/button-overlap-form-on-mobile
git branch hotfix/no-ref/registration-form-not-working
git branch test/no-ref/refactor-components-with-atomic-design
```

### Step 3 - Commit changes

Commit your changes to the branch you created in the previous step.

A commit message should start with a category of change. You can pretty much use the following 4 categories for everything: feat, fix, refactor, and chore.
Please ensure that your commit message adheres to the following format:
| Category | Detail |
| --- | --- |
| feat | Adding a new feature |
| fix | Fixing a bug |
| refactor | Changing code for performance or readability |
| chore | For everything else (documentation, formatting, tests, cleaning code, etc.) |

> Feel free to use emojis to make your commit messages more expressive. The VSCode extension [Gitmoji](https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode) is a great tool for this.

**Examples**

```bash
🎉 feat: py package scaffolding
chore: update documentation readme
feat: add new button component
fix: fix division by zero error
refactor: refactor method to improve performance
```

### Step 4 - Open pull request

Open a [pull request] to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly. Documentation is built and deployed automatically via GitHub actions.

Feel free to submit early, though — we can always iterate on this.

To run linting and code formatting checks before committing your change, you can install pre-commit as a Git hook by running the following command:

```console
$ nox --session=pre-commit -- install
```

[pull request]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/pulls

<!-- github-only -->