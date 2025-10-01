# Python Template

A modern Python project template using [uv](https://docs.astral.sh/uv/) for fast dependency management, pytest for testing, and Ruff for code quality.

## 🚀 Features

- **Fast Package Management**: Uses `uv` for lightning-fast dependency resolution and installation
- **Modern Python**: Python 3.12+ with type hints support
- **Testing Ready**: Pre-configured pytest with unit and integration test structure
- **Code Quality**: Ruff for formatting and linting
- **Type Checking**: Optional basedpyright configuration
- **Development Automation**: Makefile with common development tasks

## 📋 Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

## 🛠️ Installation

### Install uv (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd python-template

# Sync dependencies (creates .venv and installs packages)
uv sync
```

## 🎯 Usage

### Running the Application

```bash
# Using Makefile
make main

# Or directly with uv
uv run src/python-template/main.py

# Or with Python module syntax
uv run python -m python-template.main
```

### Development Commands

The project includes a `Makefile` with convenient shortcuts:

```bash
make main              # Run the main application
make test              # Run all tests (unit + integration)
make test-unit         # Run unit tests only
make test-integration  # Run integration tests only
make format            # Format code with Ruff
make lint              # Lint code with Ruff
make pre-commit        # Run pre-commit checks (unit tests + format + lint)
```

## 🧪 Testing

The project uses pytest with a clear separation between unit and integration tests:

- **Unit Tests** (`tests/unit/`): Fast, isolated tests using mocks
- **Integration Tests** (`tests/integration/`): Tests with real APIs/services

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

# With verbose output
uv run pytest -v

# With coverage
uv run pytest --cov=src/python-template
```

## 📦 Dependency Management

### Adding Dependencies

```bash
# Add runtime dependency
uv add <package-name>

# Add development dependency
uv add --dev <package-name>

# Example: Add requests library
uv add requests

# Example: Add pytest plugin
uv add --dev pytest-cov
```

### Updating Dependencies

```bash
# Update a specific package
uv lock --upgrade-package <package-name>

# Update all packages
uv lock --upgrade

# Sync after updating
uv sync
```

### Removing Dependencies

```bash
uv remove <package-name>
```

## 🎨 Code Quality

### Formatting

```bash
# Auto-format all code
make format
# or
uv run ruff format

# Check formatting without changes
uv run ruff format --check
```

### Linting

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

## 📁 Project Structure

```
.
├── src/
│   └── python-template/          # Main package source code
│       ├── __init__.py
│       └── main.py               # CLI entry point
├── tests/
│   ├── unit/                     # Unit tests with mocks
│   └── integration/              # Integration tests (real APIs/services)
├── .python-version               # Python version (3.12)
├── pyproject.toml                # Project metadata & dependencies
├── uv.lock                       # Locked dependencies (DO NOT edit manually)
├── Makefile                      # Development task automation
├── .gitignore                    # Git ignore patterns
├── AGENTS.md                     # AI coding assistant guidelines
└── README.md                     # This file
```

## 🔧 Configuration

### pyproject.toml

The `pyproject.toml` file contains:
- Project metadata (name, version, description)
- Python version requirement (>=3.12)
- Dependencies list
- Build system configuration (Hatchling)
- Tool configurations (pytest, basedpyright)

### Environment Variables

For sensitive configuration, create a `.env` file (already in `.gitignore`):

```bash
# .env
API_KEY=your-secret-key
DATABASE_URL=postgresql://localhost/db
```

Load with `python-dotenv` (already included):

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
```

## 🚀 Development Workflow

1. **Make changes** to code in `src/python-template/`
2. **Write tests** in `tests/unit/` or `tests/integration/`
3. **Run tests**: `make test`
4. **Format code**: `make format`
5. **Lint code**: `make lint`
6. **Run pre-commit checks**: `make pre-commit`
7. **Commit** your changes

## 👥 Authors

Alejandro Fernández Camello & Claude Sonnet 4.5

## 🙏 Acknowledgments

- Built with [uv](https://docs.astral.sh/uv/) for fast Python package management
- Code quality powered by [Ruff](https://github.com/astral-sh/ruff)
- Testing with [pytest](https://pytest.org/)
