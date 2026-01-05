# Quick Start Guide: Console Todo App - Phase I

## Overview

This guide explains how to set up, run, and use the Console Todo App. The application provides a command-line interface for managing todo tasks with in-memory storage.

## Prerequisites

- Python 3.14 installed
- UV package manager installed
- Terminal/shell access

## Installation

### Setting Up the Environment

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

### Starting the Application

To run the console todo app:
```bash
uv run python src/main.py
```

### Application Interface

Upon starting, you'll see the welcome menu:
```
╔════════════════════════════════╗
║     TODO CONSOLE APP v1.0      ║
╠════════════════════════════════╣
║  Commands:                     ║
║  add     - Add new task        ║
║  list    - View all tasks      ║
║  update  - Update task         ║
║  delete  - Remove task         ║
║  complete- Mark complete       ║
║  help    - Show this menu      ║
║  exit    - Exit application    ║
╚════════════════════════════════╝
```

## Usage Examples

### Adding Tasks

To add a new task:
```
> add
Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread
✓ Task #1 created: Buy groceries
```

### Viewing Tasks

To view all tasks:
```
> list
Your Tasks (1 total, 0 complete):
○ [1] Buy groceries - Milk, eggs, bread
```

### Updating Tasks

To update a task:
```
> update 1
Enter new title (leave blank to keep current): Buy groceries and fruits
Enter new description (leave blank to keep current):
✓ Task #1 updated
```

### Deleting Tasks

To delete a task:
```
> delete 1
✓ Task #1 deleted: Buy groceries and fruits
```

### Marking Tasks Complete

To mark a task complete:
```
> complete 1
✓ Task #1 marked as complete: Buy groceries and fruits
```

### Getting Help

To see available commands:
```
> help
```

### Exiting the Application

To exit the application:
```
> exit
```

## Testing

### Running Unit Tests

To run all unit tests:
```bash
uv run pytest tests/
```

### Running Tests with Coverage

To run tests with coverage reporting:
```bash
uv run pytest --cov=src tests/
```

### Type Checking

To perform type checking:
```bash
uv run mypy src/
```

## Development Workflow

### Code Formatting

To format code with Black:
```bash
uv run black src/ tests/
```

### Linting

To lint code with Ruff:
```bash
uv run ruff check src/ tests/
```

## Troubleshooting

### Common Issues

1. **Python version not found**:
   - Ensure Python 3.14 is installed and available in PATH
   - Use `uv venv --python 3.14` to create environment with correct version

2. **Import errors**:
   - Ensure virtual environment is activated
   - Run `uv pip install -e ".[dev]"` to install dependencies

3. **Permission denied**:
   - Make sure you have execute permissions on Python files
   - Run with proper privileges if needed

### Error Messages

- **"Unknown command"**: Type `help` for available commands
- **"Task #X not found"**: Task ID doesn't exist in current session
- **"Title cannot be empty"**: Task title is required
- **"Title must be 200 characters or less"**: Title exceeds maximum length
- **"Description must be 1000 characters or less"**: Description exceeds maximum length