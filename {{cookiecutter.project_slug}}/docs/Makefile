# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
APIDOC		  = sphinx-apidoc
APIDOCMODPATH = ../src/{{ cookiecutter.package_name }}
APIDOCOPTS    ?= -fMe -d 2
# APIDOCEXCLPTN ?= ../src/{{ cookiecutter.package_name }}/utils.py


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

apidoc:
	@$(APIDOC) $(APIDOCOPTS) -o "$(SOURCEDIR)/source" $(APIDOCMODPATH) $(APIDOCEXCLPTN)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
