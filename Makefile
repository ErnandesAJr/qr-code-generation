.PHONY: init
init:
	poetry install -n

.PHONY: formatting
format:
	poetry run isort --settings-path pyproject.toml ./
	poetry run black --config pyproject.toml ./

.PHONY: tests
tests:
	poetry run pytest --cov