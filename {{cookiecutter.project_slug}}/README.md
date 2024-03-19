# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}

## Description

An in-depth paragraph about the project and overview of use.

## Getting started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.


1. Install the [Databricks CLI](https://docs.databricks.com/dev-tools/cli/databricks-cli.html)

2. Authenticate to your Databricks workspace:

   ```
   $ databricks configure
   ```

Optionally, install developer tools such as the [Databricks extension for Visual Studio Code](https://docs.databricks.com/dev-tools/vscode-ext.html). Alternatively read the _getting started_ documentation for **Databricks Connect** for instructions on running the included Python code from a different IDE.

For documentation on the Databricks asset bundles format used for this project, and for CI/CD configuration, see [here](https://docs.databricks.com/dev-tools/bundles/index.html).


### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

To deploy a development copy of this project, type:

   ```
   $ databricks bundle deploy --target dev
   ```

   - Note that "dev" is the default target, so the `--target` parameter is optional here.
   - This deploys everything that's defined for this project.
   - For example, the default template would deploy a job called
   `{{ cookiecutter.package_name }}_job` to your workspace.
   - You can find the job by opening your workpace and clicking on **Workflows**.

1. Similarly, to deploy a production copy, type:

   ```
   $ databricks bundle deploy --target prod
   ```

2. To run a job or pipeline, use the "run" command:

   ```
   $ databricks bundle run
   ```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```