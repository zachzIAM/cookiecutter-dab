# cookiecutter-dab

Cookiecutter template for Databricks Asset Bundles.

## Description

This template features the following:
- Databricks Asset Bundle structure
- Python packaging and dependency management with Poetry
- Test automation with Nox
- Pre-commit hooks: ruff, prettier & darglint
- CICD with GitHub Actions
- Automated documentation with Sphinx & MyST using the furo theme & deployment to GitHub Pages
- Automated release notes with Release Drafter
- Automated dependency updates with Dependabot
- Testing and coverage with pytest
- Runtime type-checking with Typeguard
- Security audit with Safety
  
## Getting started

### Dependencies

__Databricks CLI__

1. Install the [Databricks CLI](https://docs.databricks.com/dev-tools/cli/databricks-cli.html)

2. Authenticate to your Databricks workspace:

   ```
   $ databricks configure
   ```

Optionally, install developer tools such as the [Databricks extension for Visual Studio Code](https://docs.databricks.com/dev-tools/vscode-ext.html). Alternatively read the _getting started_ documentation for **Databricks Connect** for instructions on running the included Python code from a different IDE.

For documentation on the Databricks asset bundles format used for this project, and for CI/CD configuration, see [here](https://docs.databricks.com/dev-tools/bundles/index.html).

__GitHub Repository__

In order for the GitHub Actions to work, you will need to modify some settings in your repository.

1. Go to the **Settings** tab of your repository.
2. Create two environments: `dev` and `prd`.
3. In the `prd` environment, set the deployment branch to `main` only.
4. Add the following **variables** to both environments:
   - `DATABRICKS_HOST` - The hostname of your Databricks workspace e.g. `https:// ..azuredatabricks.net`
   - `DATABRICKS_TARGET` - The target environment for the deployment. This should be _dev_ for the `dev` environment and _prd_ for the `prd` environment.
5. Add the following **secrets** to both environments:
    - `DATABRICKS_TOKEN` - The Databricks persona access token (PAT).
    - `UPLOADER_PASSWORD` - The password for the Research Team maintained Docker image used in `deploy.yml`. Required for the `databricks bundle deploy` command.

__Cookiecutter__

Cookiecutter is required to generate the project from this template.

```console
$ pip install cookiecutter
```

__Optional__

The following tools are optional but recommended for development if you opt to include a python package within your Databricks Asset Bundle.

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


### Installing

To create a new project from this template, run:

```console
$ cookiecutter https://github.com/NinetyOne-GitHub/f4-cookiecutter-dab
```

### Executing program

To deploy a development copy of this project, type:

   ```
   $ databricks bundle deploy --target dev
   ```

   - Note that "dev" is the default target, so the `--target` parameter is optional here.
   - This deploys everything that's defined for this project.
   - For example, the default template would deploy a job called
   `dab_pipeline_job` to your workspace.
   - You can find the job by opening your workpace and clicking on **Workflows**.

1. Similarly, to deploy a production copy, type:

   ```
   $ databricks bundle deploy --target prod
   ```

2. To run a job or pipeline, use the "run" command:

   ```
   $ databricks bundle run --target dev
   ```