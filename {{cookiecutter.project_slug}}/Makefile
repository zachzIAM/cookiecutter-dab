PYTHONVER   = (python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')

# set up the git hook scripts so pre-commit will run automatically on git commit
hooks:
	pre-commit install

# run the pre-commit checks manually
pre-commit:
	poetry run nox --session pre-commit-$(PYTHONVER)

# run the tests
tests:
	poetry run nox --session tests-$(PYTHONVER)
	# poetry run pytest tests -v --cov

# run all the nox sessions
nox:
	poetry run nox --python $(PYTHONVER)

# lint the code
lint:
	poetry run ruff check src tests
	poetry run ruff format src tests --check

# update dependencies
deps:
	poetry check --lock
	poetry lock --no-update

# clean up the project
clean :
	rm -rf dist *.egg-info
	coverage erase

# deploy the code to the dev environment
deploy_dev:
	databricks bundle deploy --target=dev

# deploy the code to the prod environment
deploy_prod:
	databricks bundle deploy --target=prd
