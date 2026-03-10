.PHONY: lint fmt typecheck test all clean

# Run ruff linter
lint:
	poetry run ruff check jhansi tests

# Run ruff formatter
fmt:
	poetry run ruff format jhansi tests
	poetry run ruff check --fix jhansi tests

# Run mypy typechecker
typecheck:
	poetry run mypy jhansi tests

# Run pytest
test:
	poetry run pytest -v -s

# Run all tests
all: lint fmt typecheck test

# Clean up project directories
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
