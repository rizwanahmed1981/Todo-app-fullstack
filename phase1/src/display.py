"""Display utilities for the console todo application.

This module provides formatting and output utilities for displaying tasks
and application interface elements.
"""
from typing import List
import sys

from .models import Task
from .constants import (
    MENU_HEADER, MENU_BORDER, MENU_FOOTER, MENU_TITLE,
    MENU_ITEM_FORMAT, TASK_COMPLETE_SYMBOL, TASK_INCOMPLETE_SYMBOL,
    COMMANDS, EXIT_MESSAGE, TASK_CARD_TOP_BORDER, TASK_CARD_MIDDLE_BORDER,
    TASK_CARD_BOTTOM_BORDER, TASK_CARD_LEFT_BORDER, TASK_CARD_RIGHT_BORDER,
    TASK_CARD_CORNER_TL, TASK_CARD_CORNER_TR, TASK_CARD_CORNER_BL, TASK_CARD_CORNER_BR,
    TASK_CARD_WIDTH
)

# ANSI color codes for modern color palette
ANSI_RESET = '\033[0m'
ANSI_BOLD = '\033[1m'
ANSI_DIM = '\033[2m'
ANSI_UNDERLINE = '\033[4m'
ANSI_STRIKETHROUGH = '\033[9m'

# Modern color palette
COLOR_TASK_TITLE = '\033[1;36m'  # Bold Cyan
COLOR_TASK_ID = '\033[1;33m'     # Bold Yellow
COLOR_TASK_STATUS_PENDING = '\033[31m'  # Red
COLOR_TASK_STATUS_COMPLETED = '\033[32m'  # Green
COLOR_TASK_DESCRIPTION = '\033[37m'  # White
COLOR_CARD_BORDER = '\033[36m'   # Cyan
COLOR_COMPLETED_TASK = '\033[2;37m'  # Dimmed Gray (for completed tasks)


def display_menu() -> None:
    """Display the main menu with available commands."""
    print(MENU_HEADER)
    print(MENU_TITLE)
    print(MENU_BORDER)

    for cmd, description in COMMANDS.items():
        menu_item = f"{cmd:<8} - {description}"
        print(MENU_ITEM_FORMAT.format(menu_item))

    print(MENU_FOOTER)


def display_task(task: Task, highlighted: bool = False) -> None:
    """Display a single task with enhanced card-style formatting.

    Args:
        task: The task to display
        highlighted: Whether to highlight the task (for hover/simulation effect)
    """
    # Calculate status symbol and text
    status_symbol = TASK_COMPLETE_SYMBOL if task.completed else TASK_INCOMPLETE_SYMBOL
    status_text = "COMPLETED" if task.completed else "PENDING"

    # Determine colors based on status
    status_color = COLOR_TASK_STATUS_COMPLETED if task.completed else COLOR_TASK_STATUS_PENDING

    # For completed tasks, use dimmed gray for title and description
    title_color = COLOR_COMPLETED_TASK if task.completed else COLOR_TASK_TITLE
    desc_color = COLOR_COMPLETED_TASK if task.completed else COLOR_TASK_DESCRIPTION

    # Highlight color for hover effect simulation
    highlight_bg = '\033[48;5;235m' if highlighted else ''

    # Print top border of the task card
    print(highlight_bg + COLOR_CARD_BORDER + TASK_CARD_TOP_BORDER + ANSI_RESET)

    # Print task content with colors
    if task.completed:
        # For completed tasks, apply strikethrough to title
        content_line = f"{highlight_bg}{COLOR_CARD_BORDER}{TASK_CARD_LEFT_BORDER}{ANSI_RESET} {status_symbol} {COLOR_TASK_ID}{highlight_bg}[{task.id}]{ANSI_RESET} {title_color}{ANSI_STRIKETHROUGH}{ANSI_BOLD}{highlight_bg}{task.title}{ANSI_RESET} - {status_color}{highlight_bg}{status_text}{ANSI_RESET} {COLOR_CARD_BORDER}{highlight_bg}{TASK_CARD_RIGHT_BORDER}{ANSI_RESET}"
    else:
        content_line = f"{highlight_bg}{COLOR_CARD_BORDER}{TASK_CARD_LEFT_BORDER}{ANSI_RESET} {status_symbol} {COLOR_TASK_ID}{highlight_bg}[{task.id}]{ANSI_RESET} {title_color}{ANSI_BOLD}{highlight_bg}{task.title}{ANSI_RESET} - {status_color}{highlight_bg}{status_text}{ANSI_RESET} {COLOR_CARD_BORDER}{highlight_bg}{TASK_CARD_RIGHT_BORDER}{ANSI_RESET}"
    print(content_line)

    # Print description if available
    if task.description:
        if task.completed:
            # For completed tasks, apply strikethrough to description
            desc_line = f"{highlight_bg}{COLOR_CARD_BORDER}{TASK_CARD_LEFT_BORDER}{ANSI_RESET} {desc_color}{ANSI_STRIKETHROUGH}Description: {task.description}{ANSI_RESET} {COLOR_CARD_BORDER}{highlight_bg}{TASK_CARD_RIGHT_BORDER}{ANSI_RESET}"
        else:
            desc_line = f"{highlight_bg}{COLOR_CARD_BORDER}{TASK_CARD_LEFT_BORDER}{ANSI_RESET} {desc_color}Description: {task.description}{ANSI_RESET} {COLOR_CARD_BORDER}{highlight_bg}{TASK_CARD_RIGHT_BORDER}{ANSI_RESET}"

        # Truncate if too long to fit in card
        if len(desc_line) > TASK_CARD_WIDTH:
            desc_line = desc_line[:TASK_CARD_WIDTH-4] + "... " + highlight_bg + COLOR_CARD_BORDER + TASK_CARD_RIGHT_BORDER + ANSI_RESET
        print(desc_line)

    # Print bottom border of the task card
    print(highlight_bg + COLOR_CARD_BORDER + TASK_CARD_BOTTOM_BORDER + ANSI_RESET)


def display_tasks(tasks: List[Task]) -> None:
    """Display a list of tasks with enhanced card-style formatting.

    Args:
        tasks: The list of tasks to display
    """
    if not tasks:
        print("No tasks found.")
        return

    # Count completed tasks
    completed_count = sum(1 for task in tasks if task.completed)
    total_count = len(tasks)

    print(f"\nYour Tasks ({total_count} total, {completed_count} complete):\n")

    for i, task in enumerate(tasks):
        display_task(task)
        # Add spacing between cards, but not after the last one
        if i < len(tasks) - 1:
            print()  # Add a blank line between task cards


def display_message(message: str) -> None:
    """Display a simple message to the user.

    Args:
        message: The message to display
    """
    print(message)


def display_exit_message() -> None:
    """Display the exit message when the application closes."""
    print(EXIT_MESSAGE)