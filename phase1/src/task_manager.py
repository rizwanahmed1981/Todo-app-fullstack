"""Task manager for the console todo application.

This module handles the business logic and data management for tasks.
It provides functionality for adding, listing, updating, deleting, and completing tasks.
"""
from datetime import datetime
from typing import Dict, List, Optional

from .models import Task, TaskNotFoundError, ValidationError
from .constants import TITLE_MIN_LENGTH, TITLE_MAX_LENGTH, DESCRIPTION_MAX_LENGTH


class TaskManager:
    """Manages tasks in memory with core business logic."""

    def __init__(self) -> None:
        """Initialize the task manager with empty storage and next ID counter."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def _validate_title(self, title: str) -> None:
        """Validate the title according to business rules.

        Args:
            title: The title to validate

        Raises:
            ValidationError: If the title doesn't meet requirements
        """
        if not title or not title.strip():
            raise ValidationError("Title cannot be empty.")

        title_stripped = title.strip()
        if len(title_stripped) < TITLE_MIN_LENGTH:
            raise ValidationError("Title cannot be empty.")

        if len(title_stripped) > TITLE_MAX_LENGTH:
            raise ValidationError(f"Title must be {TITLE_MAX_LENGTH} characters or less.")

    def _validate_description(self, description: Optional[str]) -> None:
        """Validate the description according to business rules.

        Args:
            description: The description to validate

        Raises:
            ValidationError: If the description doesn't meet requirements
        """
        if description is not None and len(description) > DESCRIPTION_MAX_LENGTH:
            raise ValidationError(f"Description must be {DESCRIPTION_MAX_LENGTH} characters or less.")

    def _generate_next_id(self) -> int:
        """Generate the next unique task ID.

        Returns:
            The next unique task ID
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task with the given title and optional description.

        Args:
            title: The title of the task (required)
            description: The description of the task (optional)

        Returns:
            The created Task object

        Raises:
            ValidationError: If the title or description don't meet requirements
        """
        # Validate inputs
        self._validate_title(title)
        self._validate_description(description)

        # Create task with unique ID
        task_id = self._generate_next_id()
        task = Task(
            id=task_id,
            title=title.strip(),
            description=description,
            completed=False,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        # Store task
        self._tasks[task_id] = task
        return task

    def list_tasks(self) -> List[Task]:
        """List all tasks in creation order.

        Returns:
            A list of all tasks sorted by creation order
        """
        # Return tasks sorted by ID (creation order)
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_task(self, task_id: int) -> Task:
        """Get a specific task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task with the given ID

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        return self._tasks[task_id]

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """Update a task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated Task object

        Raises:
            TaskNotFoundError: If no task exists with the given ID
            ValidationError: If the new title or description don't meet requirements
        """
        # Validate inputs if provided
        if title is not None:
            self._validate_title(title)
            title = title.strip()
        if description is not None:
            self._validate_description(description)

        # Get existing task
        task = self.get_task(task_id)

        # Update task
        task.update(title=title, description=description)
        return task

    def delete_task(self, task_id: int) -> Task:
        """Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            The deleted Task object

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        task = self.get_task(task_id)
        del self._tasks[task_id]
        return task

    def complete_task(self, task_id: int) -> Task:
        """Toggle a task's completion status.

        Args:
            task_id: The ID of the task to mark complete/incomplete

        Returns:
            The updated Task object

        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        task = self.get_task(task_id)
        task.mark_complete()
        return task