# BASIC INSTRUCTIONS

This document provides comprehensive guidance for AI coding assistants working on this Python project. It covers project structure, tooling, testing patterns, and development workflows.

## Project Overview

**Technology Stack:**
- **Language**: Python 3.12+
- **Package Manager**: [uv](https://docs.astral.sh/uv/) (fast Python package manager)
- **Build System**: Hatchling
- **Testing**: pytest
- **Code Quality**: Ruff (formatting & linting)
- **Type Checking**: basedpyright (optional)

## Repository Structure

```
.
├── src/
│   └── <package_name>/          # Main package source code
│       ├── __init__.py
│       ├── main.py              # CLI entry point
│       └── *.py                 # Module files
├── tests/
│   ├── unit/                    # Unit tests with mocks
│   │   └── test_*.py
│   └── integration/             # Integration tests (real APIs/services)
│       └── test_*.py
├── .python-version              # Python version (e.g., 3.12)
├── pyproject.toml               # Project metadata & dependencies
├── uv.lock                      # Locked dependencies (DO NOT edit manually)
├── Makefile                     # Development task automation
├── .gitignore                   # Git ignore patterns
└── README.md                    # Project documentation
```

## Development Workflow with uv

### Initial Setup

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone repository and navigate to it
cd <project-directory>

# Sync dependencies (creates .venv and installs packages)
uv sync
```

### Common uv Commands

| Command | Purpose |
|---------|---------|
| `uv sync` | Install/sync all dependencies from lockfile to `.venv` |
| `uv add <package>` | Add a new dependency to `pyproject.toml` and install it |
| `uv add --dev <package>` | Add a development dependency |
| `uv remove <package>` | Remove a dependency |
| `uv run <command>` | Run a command in the project environment (auto-syncs) |
| `uv lock` | Update the lockfile without installing |
| `uv lock --upgrade-package <pkg>` | Upgrade a specific package |
| `uv python install 3.12` | Install a specific Python version |

### Running Code

```bash
# Run a Python script (uv handles environment automatically)
uv run python -m <package_name>.main

# Run with arguments
uv run python -m <package_name>.main --arg value

# Run any command in the project environment
uv run <command>
```

**Note**: `uv run` automatically ensures the environment is synced before execution. No need to manually activate the virtual environment.

### Manual Environment Activation (Optional)

If you prefer traditional workflow:

```bash
# Sync first
uv sync

# Activate virtual environment
source .venv/bin/activate  # Unix/macOS
# or
.venv\Scripts\activate     # Windows

# Run commands directly
python -m <package_name>.main
pytest tests/
```

## Makefile Targets

The `Makefile` provides convenient shortcuts for common tasks:

```makefile
test: test-unit test-integration
	@echo "All tests completed successfully"

pre-commit: test-unit format lint
	@echo "Pre-commit checks passed"

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
```

**Usage:**
```bash
make test           # Run all tests
make test-unit      # Unit tests only
make test-integration  # Integration tests only
make format         # Auto-format code
make lint           # Check code quality
make pre-commit     # Run before committing
```

## Testing Strategy

### Test Organization

- **Unit Tests** (`tests/unit/`): Fast, isolated tests using mocks
  - Test individual functions/classes in isolation
  - Use `unittest.mock.Mock` for external dependencies
  - Should run in milliseconds

- **Integration Tests** (`tests/integration/`): Test real interactions
  - Test with actual APIs, databases, or external services
  - May require API keys or running services
  - Slower but verify real-world behavior
  - Don't mock anything in integration tests unless explicitly required by the user

### Testing Patterns

#### 1. Using pytest Fixtures

```python
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_api_client():
    """Create a mock API client."""
    client = Mock()
    client.fetch_data.return_value = {"status": "success"}
    return client

def test_function_with_mock(mock_api_client):
    result = my_function(mock_api_client)
    assert result == expected_value
    mock_api_client.fetch_data.assert_called_once()
```

#### 2. Parametrized Tests

```python
@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (1, 2),
        (5, 10),
        (0, 0),
    ],
)
def test_function_with_params(input_value, expected_output):
    assert my_function(input_value) == expected_output
```

#### 3. Testing Exceptions

```python
def test_invalid_input_raises():
    with pytest.raises(ValueError):
        my_function(invalid_input)
```

#### 4. Integration Test Example

```python
def test_api_integration():
    """Test with real API (requires API key in environment)."""
    client = create_api_client()
    result = client.fetch_data()
    
    assert isinstance(result, dict)
    assert "status" in result
```

### Running Tests

```bash
# All tests
make test
# or
uv run pytest

# Unit tests only
make test-unit
# or
uv run pytest tests/unit

# Integration tests only
make test-integration
# or
uv run pytest tests/integration

# Run specific test file
uv run pytest tests/unit/test_specific.py

# Run with verbose output
uv run pytest -v

# Run with coverage
uv run pytest --cov=src/<package_name>
```

## Code Quality

### Formatting with Ruff

```bash
# Auto-format all code
make format
# or
uv run ruff format

# Check formatting without changes
uv run ruff format --check
```

### Linting with Ruff

```bash
# Run linter
make lint
# or
uv run ruff check

# Auto-fix issues where possible
uv run ruff check --fix
```

### Pre-commit Checks

Before committing code, run:

```bash
make pre-commit
```

This runs unit tests, formatting, and linting to ensure code quality.

## Project Configuration (pyproject.toml)

### Basic Structure

```toml
[project]
name = "package-name"
version = "0.1.0"
description = "Package description"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "package1>=1.0.0",
    "package2>=2.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/<package_name>"]

[tool.pytest.ini_options]
addopts = "-v --capture=no"

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W"]
ignore = []
```

### Adding Dependencies

**Runtime dependencies:**
```bash
uv add requests
uv add "pandas>=2.0.0"
```

**Development dependencies:**
```bash
uv add --dev pytest
uv add --dev ruff
```

**From requirements.txt:**
```bash
uv add -r requirements.txt
```

## Code Organization Patterns

### 1. Protocol-Based Interfaces

Use protocols for dependency injection and testing:

```python
from typing import Protocol

class DataProvider(Protocol):
    """Protocol for data providers."""
    
    def fetch_data(self, query: str) -> dict: ...

class MyService:
    def __init__(self, provider: DataProvider):
        self.provider = provider
    
    def process(self, query: str):
        data = self.provider.fetch_data(query)
        return self._transform(data)
```

### 2. Dataclasses for Data Structures

```python
from dataclasses import dataclass

@dataclass
class Result:
    """Result of an operation."""
    success: bool
    data: dict
    error_message: str | None = None
```

### 3. CLI Entry Point

```python
#!/usr/bin/env python3
"""Main CLI entry point."""

import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument("--option", type=str, help="Option help")
    args = parser.parse_args()
    
    try:
        # Main logic
        pass
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### 4. Module Organization

```python
# src/package_name/
├── __init__.py          # Package initialization
├── main.py              # CLI entry point
├── core.py              # Core business logic
├── models.py            # Data models (dataclasses, protocols)
├── api.py               # External API integrations
├── utils.py             # Utility functions
└── config.py            # Configuration management
```

## Environment Variables

Use `.env` file for sensitive configuration (add to `.gitignore`):

```bash
# .env
API_KEY=your-secret-key
DATABASE_URL=postgresql://localhost/db
```

Load with `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
```

## Git Ignore Patterns

Standard `.gitignore` for Python projects:

```gitignore
# Virtual environment
.venv
venv/
ENV/

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.so

# Testing
.pytest_cache/
.coverage
htmlcov/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment variables
.env
.env.local

# Build artifacts
dist/
build/
*.egg-info/

# uv
.ruff_cache/
```

## Common Development Tasks

### Adding a New Feature

1. Add dependencies if needed: `uv add <package>`
2. Implement feature in `src/<package_name>/`
3. Write unit tests in `tests/unit/test_<feature>.py`
4. Write integration tests if needed in `tests/integration/`
5. Run tests: `make test`
6. Format and lint: `make format && make lint`

### Updating Dependencies

```bash
# Update a specific package
uv lock --upgrade-package requests

# Update all packages (careful!)
uv lock --upgrade

# Sync after updating
uv sync
```

### Debugging

```bash
# Run with Python debugger
uv run python -m pdb -m <package_name>.main

# Run tests with output
uv run pytest -s -v

# Run specific test with debugging
uv run pytest tests/unit/test_file.py::test_function -s
```

## Best Practices

### 1. Type Hints

Use type hints for better code clarity and IDE support:

```python
from typing import Literal

def process_data(
    data: list[dict],
    mode: Literal["fast", "accurate"] = "fast"
) -> dict[str, int]:
    """Process data and return statistics."""
    return {"count": len(data)}
```

### 2. Error Handling

Be explicit with error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise RuntimeError("Operation failed") from e
```

### 3. Documentation

Use docstrings for modules, classes, and functions ALWAYS:

```python
def calculate_score(
    correct: int,
    total: int,
    weight: float = 1.0
) -> float:
    """
    Calculate weighted score.
    
    Args:
        correct: Number of correct answers.
        total: Total number of questions.
        weight: Score weight multiplier.
    
    Returns:
        Weighted score between 0 and 1.
    
    Raises:
        ValueError: If total is zero or negative.
    """
    if total <= 0:
        raise ValueError("Total must be positive")
    return (correct / total) * weight
```

### 4. Testing Philosophy

- **Write tests first** (TDD) when possible
- **Mock external dependencies** in unit tests
- **Test edge cases** and error conditions
- **Keep tests fast** - unit tests should run in milliseconds
- **Integration tests** should verify real-world scenarios

## Troubleshooting

### Common Issues

**Issue**: `uv sync` fails with dependency conflicts
```bash
# Solution: Check pyproject.toml for conflicting versions
# Update specific package
uv lock --upgrade-package problematic-package
```

**Issue**: Tests fail with import errors
```bash
# Solution: Ensure package is installed in editable mode
uv sync
# Or explicitly
uv pip install -e .
```

**Issue**: Ruff formatting conflicts
```bash
# Solution: Check .ruff.toml or [tool.ruff] in pyproject.toml
# Run format to auto-fix
uv run ruff format
```

## Additional Resources

- **uv Documentation**: https://docs.astral.sh/uv/
- **pytest Documentation**: https://docs.pytest.org/
- **Ruff Documentation**: https://docs.astral.sh/ruff/
- **Python Packaging Guide**: https://packaging.python.org/

## AI Assistant Guidelines

When working on this project:

1. **Always use `uv run`** for executing Python commands
2. **Run tests** after making changes: `make test-unit`
3. **Format code** before committing: `make format`
4. **Check linting**: `make lint`
5. **Update tests** when modifying functionality
6. **Use type hints** for new functions
7. **Follow existing patterns** in the codebase
8. **Add docstrings** for public APIs
9. **Mock external dependencies** in unit tests
10. **Keep integration tests separate** from unit tests

### Making Changes

When implementing new features:
- Add dependencies with `uv add <package>`
- Create corresponding test files
- Use protocols for interfaces
- Use dataclasses for data structures
- Follow the existing module organization
- Run `make pre-commit` before finishing

### Testing Checklist

- [ ] Unit tests pass: `make test-unit`
- [ ] Integration tests pass (if applicable): `make test-integration`
- [ ] Code formatted: `make format`
- [ ] Linting passes: `make lint`
- [ ] Type hints added for new functions
- [ ] Docstrings added for public APIs
- [ ] Edge cases tested
- [ ] Error handling tested
