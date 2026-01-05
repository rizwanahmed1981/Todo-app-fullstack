"""Data models for the console todo application.

This module defines the Task dataclass and custom exceptions for the application.
Based on the data-model.md specification.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Represents a single todo item in the console application.

    Attributes:
        id: Unique identifier for the task
        title: Title of the task (1-200 characters)
        description: Detailed description of the task (max 1000 characters, optional)
        completed: Boolean indicating if task is complete
        created_at: Timestamp when task was created
        updated_at: Timestamp when task was last updated
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self) -> None:
        """Initialize timestamps if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    def mark_complete(self) -> None:
        """Toggle the completion status and update the timestamp."""
        self.completed = not self.completed
        self.updated_at = datetime.now()

    def update(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
        """Update task title and/or description and update the timestamp.

        Args:
            title: New title (optional)
            description: New description (optional)
        """
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.updated_at = datetime.now()


class TaskNotFoundError(Exception):
    """Exception raised when attempting to access a task that doesn't exist."""

    def __init__(self, task_id: int) -> None:
        """Initialize the exception with the task ID that was not found.

        Args:
            task_id: The ID of the task that was not found
        """
        super().__init__(f"Task #{task_id} not found.")


class ValidationError(Exception):
    """Exception raised when invalid input data is provided for task creation or update."""

    def __init__(self, message: str) -> None:
        """Initialize the exception with an error message.

        Args:
            message: The error message describing the validation issue
        """
        super().__init__(message)