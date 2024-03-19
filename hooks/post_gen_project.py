import os
import shutil


def delete_docs_folder_if_requested():
    generate_docs = "{{ cookiecutter.automated_sphinx_docs }}".lower()
    sphinx_docs_folder = "docs"
    gh_actions_docs_file = ".github/workflows/documentation.yml"

    if generate_docs == "n":
        if os.path.exists(sphinx_docs_folder):
            shutil.rmtree(sphinx_docs_folder)
            print("Deleted /docs folder based on user choice.")
        else:
            print("/docs folder not found. No action required.")

        if os.path.exists(gh_actions_docs_file):
            os.remove(gh_actions_docs_file)
            print("Deleted github actions file for documentation.")
        else:
            print("/docs folder not found. No action required.")
    else:
        print("Retaining /docs folder based on user choice.")


def delete_issue_template_folder_if_requested():
    github_issue_template = "{{ cookiecutter.github_issue_template }}".lower()
    github_issue_folder = ".github/workflows/ISSUE_TEMPLATE"
    if github_issue_template == "n":
        if os.path.exists(github_issue_folder):
            shutil.rmtree(github_issue_folder)
            print(
                "Deleted .github/workflows/ISSUE_TEMPLATE folder based on user choice."
            )
        else:
            print(
                ".github/workflows/ISSUE_TEMPLATE folder not found. No action required."
            )


def delete_py_package_if_requested():
    inc_python_package = "{{ cookiecutter.inc_python_package }}".lower()
    py_package_folders = [
        "src/{{ cookiecutter.package_name }}",
        "tests",
        "examples",
        "scratch",
    ]
    py_package_related_files = [
        ".github/workflows/constraints.txt",
        ".github/workflows/labeler.yml",
        ".github/workflows/release.yml",
        ".github/workflows/tests.yml",
        ".github/dependabot.yml",
        ".github/labels.yml",
        ".github/release-drafter.yml",
        ".darglint",
        ".pre-commit-config.yaml",
        "CONTRIBUTING.md",
        "Makefile",
        "noxfile.py",
        "pyproject.toml",
    ]

    if inc_python_package == "n":
        for i in py_package_folders:
            shutil.rmtree(i)
        for i in py_package_related_files:
            os.remove(i)


def main():
    delete_docs_folder_if_requested()

    delete_issue_template_folder_if_requested()

    delete_py_package_if_requested()


if __name__ == "__main__":
    main()
