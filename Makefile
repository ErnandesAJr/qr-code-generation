.PHONY: init format running tests
init:
	poetry install -n

format:
	poetry run isort --settings-path pyproject.toml ./
	poetry run black --config pyproject.toml ./

running:
	PYTHONPATH=src poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

tests:
	poetry run pytest --cov