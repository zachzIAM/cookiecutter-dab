hooks:
	pre-commit install

lint:
	poetry run ruff check src tests
	poetry run ruff format src tests --check

format:
	poetry run ruff check src tests --fix
	poetry run ruff format src tests

deps:
	poetry check --lock
	poetry lock --no-update

test:
	poetry run pytest tests -v --cov

clean :
	rm -rf dist *.egg-info
	coverage erase

deploy_dev:
	databricks bundle deploy --target=dev
	databricks bundle run --target=dev

deploy_prod:
	databricks bundle deploy --target=prod
