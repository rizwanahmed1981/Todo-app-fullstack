"""Unit tests for the models module.

This module tests the Task dataclass and custom exceptions.
"""
import pytest
from datetime import datetime

from src.models import Task, TaskNotFoundError, ValidationError


class TestTask:
    """Test cases for the Task dataclass."""

    def test_task_creation(self) -> None:
        """Test creating a task with all attributes."""
        task_id = 1
        title = "Test Task"
        description = "Test Description"
        completed = False
        created_at = datetime(2023, 1, 1, 12, 0, 0)
        updated_at = datetime(2023, 1, 1, 12, 0, 0)

        task = Task(
            id=task_id,
            title=title,
            description=description,
            completed=completed,
            created_at=created_at,
            updated_at=updated_at
        )

        assert task.id == task_id
        assert task.title == title
        assert task.description == description
        assert task.completed == completed
        assert task.created_at == created_at
        assert task.updated_at == updated_at

    def test_task_creation_with_defaults(self) -> None:
        """Test creating a task with default values."""
        task = Task(id=1, title="Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description is None
        assert task.completed is False
        assert task.created_at is not None
        assert task.updated_at is not None

    def test_task_mark_complete(self) -> None:
        """Test marking a task as complete/incomplete."""
        task = Task(id=1, title="Test Task", completed=False)

        # Mark as complete
        task.mark_complete()
        assert task.completed is True

        # Mark as incomplete
        task.mark_complete()
        assert task.completed is False

    def test_task_update(self) -> None:
        """Test updating a task's title and description."""
        task = Task(id=1, title="Original Title", description="Original Description")

        new_title = "Updated Title"
        new_description = "Updated Description"

        task.update(title=new_title, description=new_description)

        assert task.title == new_title
        assert task.description == new_description

    def test_task_update_partial(self) -> None:
        """Test updating only title or description."""
        task = Task(id=1, title="Original Title", description="Original Description")

        # Update only title
        task.update(title="New Title")
        assert task.title == "New Title"
        assert task.description == "Original Description"

        # Update only description
        task.update(description="New Description")
        assert task.title == "New Title"
        assert task.description == "New Description"

    def test_task_timestamp_update(self) -> None:
        """Test that timestamps are updated when task is modified."""
        original_time = datetime(2023, 1, 1, 12, 0, 0)
        task = Task(id=1, title="Test Task", created_at=original_time, updated_at=original_time)

        initial_updated_at = task.updated_at

        # Update task and check that updated_at changed
        task.update(title="Updated Title")
        assert task.updated_at != initial_updated_at


class TestTaskNotFoundError:
    """Test cases for the TaskNotFoundError exception."""

    def test_task_not_found_error(self) -> None:
        """Test that TaskNotFoundError is raised with correct message."""
        task_id = 42
        error = TaskNotFoundError(task_id)

        expected_message = f"Task #{task_id} not found."
        assert str(error) == expected_message


class TestValidationError:
    """Test cases for the ValidationError exception."""

    def test_validation_error(self) -> None:
        """Test that ValidationError is raised with correct message."""
        message = "Invalid input provided"
        error = ValidationError(message)

        assert str(error) == message