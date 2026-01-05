"""Test that the application can be imported and run."""
import sys
from pathlib import Path

# Add the src directory to the path so we can import modules
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports() -> None:
    """Test that all modules can be imported successfully."""
    from src.models import Task, TaskNotFoundError, ValidationError
    from src.task_manager import TaskManager
    from src.display import display_menu, display_tasks, display_message
    from src.main import main

    # Test that we can create instances
    task = Task(id=1, title="Test")
    task_manager = TaskManager()

    # Test that functions exist
    assert callable(display_menu)
    assert callable(display_tasks)
    assert callable(display_message)
    assert callable(main)

    print("All imports successful!")

if __name__ == "__main__":
    test_imports()