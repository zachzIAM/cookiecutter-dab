"""Sphinx configuration."""

import importlib.metadata

# Path setup
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime


sys.path.insert(0, os.path.abspath("../src/{{ cookiecutter.package_name }}/"))

# Project information.
project = "{{ cookiecutter.project_name }}"
author = "{{ cookiecutter.author }}"
copyright = f"{datetime.now().year}, {{ cookiecutter.author }}"
version = importlib.metadata.version("{{ cookiecutter.package_name }}")
release = importlib.metadata.version("{{ cookiecutter.package_name }}")

extensions = [
    "sphinx.ext.autodoc",  # automatically generate documentation for modules
    "sphinx.ext.napoleon",  # to read Google-style or Numpy-style docstrings
    "sphinx.ext.mathjax",  # to allow the use of math in the documentation
    "sphinx.ext.viewcode",  # to allow vieing the source code in the web page
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
