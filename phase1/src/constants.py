"""Constants for the console todo application.

This module defines application constants and UI formatting strings.
"""

# Task validation constants
TITLE_MIN_LENGTH = 1
TITLE_MAX_LENGTH = 200
DESCRIPTION_MAX_LENGTH = 1000

# UI formatting constants
WELCOME_MESSAGE = "TODO CONSOLE APP v1.0"
MENU_HEADER = "╔════════════════════════════════╗"
MENU_BORDER = "╠════════════════════════════════╣"
MENU_FOOTER = "╚════════════════════════════════╝"
MENU_TITLE = f"║     {WELCOME_MESSAGE:<26} ║"
MENU_ITEM_FORMAT = "║  {:<27} ║"
EXIT_MESSAGE = "Goodbye! Thanks for using the Todo Console App."

# Command constants
COMMANDS = {
    "add": "Add new task",
    "list": "View all tasks",
    "update": "Update task",
    "delete": "Remove task",
    "complete": "Mark complete",
    "help": "Show this menu",
    "exit": "Exit application"
}

# Display constants
TASK_INCOMPLETE_SYMBOL = "○"
TASK_COMPLETE_SYMBOL = "●"

# Enhanced card-style display constants for task items
TASK_CARD_WIDTH = 60
TASK_CARD_TOP_BORDER = "┌" + "─" * (TASK_CARD_WIDTH - 2) + "┐"
TASK_CARD_MIDDLE_BORDER = "├" + "─" * (TASK_CARD_WIDTH - 2) + "┤"
TASK_CARD_BOTTOM_BORDER = "└" + "─" * (TASK_CARD_WIDTH - 2) + "┘"
TASK_CARD_LEFT_BORDER = "│"
TASK_CARD_RIGHT_BORDER = "│"
TASK_CARD_CORNER_TL = "┌"
TASK_CARD_CORNER_TR = "┐"
TASK_CARD_CORNER_BL = "└"
TASK_CARD_CORNER_BR = "┘"