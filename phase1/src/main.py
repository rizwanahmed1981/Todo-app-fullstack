"""Main entry point for the console todo application.

This module implements the console interface and command loop for the application.
"""
import sys
from typing import Optional

# Import using relative paths to work correctly when run as a module
from .task_manager import TaskManager
from .display import display_menu, display_tasks, display_message, display_exit_message
from .models import ValidationError


def main() -> None:
    """Main entry point for the console todo application."""
    print("Starting Todo Console App...")

    task_manager = TaskManager()

    print("Welcome to the Todo Console App!")
    display_menu()

    while True:
        try:
            command = input("\n> ").strip().lower()

            if command == "exit":
                handle_exit()
            elif command == "help":
                handle_help()
            elif command == "list":
                handle_list(task_manager)
            elif command == "add":
                handle_add(task_manager)
            elif command == "update":
                handle_update(task_manager)
            elif command == "delete":
                handle_delete(task_manager)
            elif command == "complete":
                handle_complete(task_manager)
            else:
                display_message(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            handle_exit()
        except EOFError:
            handle_exit()


def handle_add(task_manager: TaskManager) -> None:
    """Handle the add command to create a new task.

    Args:
        task_manager: The task manager instance to use for adding tasks
    """
    try:
        title = input("Enter task title: ").strip()

        description_input = input("Enter task description (optional): ").strip()
        description = description_input if description_input else None

        task = task_manager.add_task(title, description)
        display_message(f"✓ Task #{task.id} created: {task.title}")

    except ValidationError as e:
        display_message(f"Error: {e}")
    except Exception as e:
        display_message(f"Unexpected error: {e}")


def handle_list(task_manager: TaskManager) -> None:
    """Handle the list command to display all tasks.

    Args:
        task_manager: The task manager instance to use for listing tasks
    """
    try:
        tasks = task_manager.list_tasks()
        display_tasks(tasks)
    except Exception as e:
        display_message(f"Error listing tasks: {e}")


def handle_update(task_manager: TaskManager) -> None:
    """Handle the update command to modify a task.

    Args:
        task_manager: The task manager instance to use for updating tasks
    """
    try:
        task_id_input = input("Enter task ID to update: ").strip()
        if not task_id_input.isdigit():
            display_message("Error: Task ID must be a number.")
            return

        task_id = int(task_id_input)

        # Get current task to show current values
        current_task = task_manager.get_task(task_id)

        new_title_input = input(f"Enter new title (leave blank to keep '{current_task.title}'): ").strip()
        new_title: Optional[str] = new_title_input if new_title_input else None  # Use None to keep current

        new_desc_input = input("Enter new description (leave blank to keep current): ").strip()
        new_desc: Optional[str] = new_desc_input if new_desc_input else None  # Use None to keep current

        # Only update if user provided new values
        title_to_use = new_title if new_title is not None else current_task.title
        desc_to_use = new_desc if new_desc is not None else current_task.description

        task = task_manager.update_task(task_id, title_to_use, desc_to_use)
        display_message(f"✓ Task #{task.id} updated")

    except ValidationError as e:
        display_message(f"Error: {e}")
    except Exception as e:
        display_message(f"Error updating task: {e}")


def handle_delete(task_manager: TaskManager) -> None:
    """Handle the delete command to remove a task.

    Args:
        task_manager: The task manager instance to use for deleting tasks
    """
    try:
        task_id_input = input("Enter task ID to delete: ").strip()
        if not task_id_input.isdigit():
            display_message("Error: Task ID must be a number.")
            return

        task_id = int(task_id_input)

        task = task_manager.delete_task(task_id)
        display_message(f"✓ Task #{task.id} deleted: {task.title}")

    except Exception as e:
        display_message(f"Error deleting task: {e}")


def handle_complete(task_manager: TaskManager) -> None:
    """Handle the complete command to toggle a task's completion status.

    Args:
        task_manager: The task manager instance to use for completing tasks
    """
    try:
        task_id_input = input("Enter task ID to mark complete/incomplete: ").strip()
        if not task_id_input.isdigit():
            display_message("Error: Task ID must be a number.")
            return

        task_id = int(task_id_input)

        task = task_manager.complete_task(task_id)
        status = "complete" if task.completed else "incomplete"
        display_message(f"✓ Task #{task.id} marked as {status}: {task.title}")

    except Exception as e:
        display_message(f"Error completing task: {e}")


def handle_help() -> None:
    """Handle the help command to display available commands."""
    display_menu()


def handle_exit() -> None:
    """Handle the exit command to terminate the application."""
    display_exit_message()
    sys.exit(0)


if __name__ == "__main__":
    main()