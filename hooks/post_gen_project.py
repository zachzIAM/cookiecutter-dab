import os
import shutil


def remove_open_source_files():
    file_names = ["LICENSE"]
    for file_name in file_names:
        os.remove(file_name)


def delete_docs_folder_if_requested():
    generate_docs = "{{ cookiecutter.automated_sphinx_docs }}".lower()
    docs_folder = "docs"

    if generate_docs == "n":
        if os.path.exists(docs_folder):
            shutil.rmtree(docs_folder)
            print("Deleted /docs folder based on user choice.")
        else:
            print("/docs folder not found. No action required.")
    else:
        print("Retaining /docs folder based on user choice.")


def main():
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    delete_docs_folder_if_requested()


if __name__ == "__main__":
    main()
