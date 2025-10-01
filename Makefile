main:
	@echo "Running main..."
	uv run src/python-template/main.py

test: test-unit test-integration
	@echo "All tests completed successfully"

pre-commit: test-unit format lint

test-unit:
	@echo "Running unit tests..."
	uv run pytest -s tests/unit

test-integration:
	@echo "Running integration tests..."
	uv run pytest -s tests/integration

format:
	@echo "Formatting code..."
	uv run ruff format

lint:
	@echo "Running linter..."
	uv run ruff check
