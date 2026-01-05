# Console Todo App - Phase I

This is a console-based todo application with in-memory storage, supporting the five core features: Add, List, Update, Delete, and Complete tasks.

## Prerequisites

- Python 3.14
- UV package manager

## Setup

1. Navigate to the project directory:
   ```bash
   cd phase1
   ```

2. Create a Python virtual environment with Python 3.14:
   ```bash
   uv venv --python 3.14
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

4. Install development dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```

## Running the Application

To run the console todo app:
```bash
uv run python src/main.py
```

## Running Tests

To run all unit tests:
```bash
uv run pytest tests/
```

To run tests with coverage reporting:
```bash
uv run pytest --cov=src tests/
```

## Development Commands

- Format code: `uv run black src/ tests/`
- Lint code: `uv run ruff check src/ tests/`
- Type check: `uv run mypy src/`