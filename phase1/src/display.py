"""Display utilities for the console todo application.

This module provides formatting and output utilities for displaying tasks
and application interface elements.
"""
from typing import List

from .models import Task
from .constants import (
    MENU_HEADER, MENU_BORDER, MENU_FOOTER, MENU_TITLE,
    MENU_ITEM_FORMAT, TASK_COMPLETE_SYMBOL, TASK_INCOMPLETE_SYMBOL,
    COMMANDS, EXIT_MESSAGE
)


def display_menu() -> None:
    """Display the main menu with available commands."""
    print(MENU_HEADER)
    print(MENU_TITLE)
    print(MENU_BORDER)

    for cmd, description in COMMANDS.items():
        menu_item = f"{cmd:<8} - {description}"
        print(MENU_ITEM_FORMAT.format(menu_item))

    print(MENU_FOOTER)


def display_task(task: Task) -> None:
    """Display a single task with formatting.

    Args:
        task: The task to display
    """
    status_symbol = TASK_COMPLETE_SYMBOL if task.completed else TASK_INCOMPLETE_SYMBOL
    status_text = "COMPLETED" if task.completed else "PENDING"

    print(f"{status_symbol} [{task.id}] {task.title} - {status_text}")
    if task.description:
        print(f"    Description: {task.description}")


def display_tasks(tasks: List[Task]) -> None:
    """Display a list of tasks with formatting.

    Args:
        tasks: The list of tasks to display
    """
    if not tasks:
        print("No tasks found.")
        return

    # Count completed tasks
    completed_count = sum(1 for task in tasks if task.completed)
    total_count = len(tasks)

    print(f"Your Tasks ({total_count} total, {completed_count} complete):")

    for task in tasks:
        display_task(task)
        print()  # Add a blank line between tasks


def display_message(message: str) -> None:
    """Display a simple message to the user.

    Args:
        message: The message to display
    """
    print(message)


def display_exit_message() -> None:
    """Display the exit message when the application closes."""
    print(EXIT_MESSAGE)