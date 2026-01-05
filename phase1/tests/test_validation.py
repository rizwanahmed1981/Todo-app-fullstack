"""Unit tests for validation functionality.

This module tests the validation logic in the task manager.
"""
import pytest
from datetime import datetime

from src.models import TaskNotFoundError, ValidationError
from src.task_manager import TaskManager


class TestTaskValidation:
    """Test cases for task validation."""

    def test_validate_empty_title(self) -> None:
        """Test that empty titles are rejected."""
        task_manager = TaskManager()

        with pytest.raises(ValidationError, match="Title cannot be empty."):
            task_manager.add_task("")

    def test_validate_whitespace_only_title(self) -> None:
        """Test that whitespace-only titles are rejected."""
        task_manager = TaskManager()

        with pytest.raises(ValidationError, match="Title cannot be empty."):
            task_manager.add_task("   ")

    def test_validate_long_title(self) -> None:
        """Test that titles exceeding max length are rejected."""
        task_manager = TaskManager()
        long_title = "A" * 201  # Exceeds the 200 character limit

        with pytest.raises(ValidationError, match="Title must be 200 characters or less."):
            task_manager.add_task(long_title)

    def test_validate_long_description(self) -> None:
        """Test that descriptions exceeding max length are rejected."""
        task_manager = TaskManager()
        long_description = "A" * 1001  # Exceeds the 1000 character limit

        with pytest.raises(ValidationError, match="Description must be 1000 characters or less."):
            task_manager.add_task("Valid Title", long_description)

    def test_valid_title_and_description(self) -> None:
        """Test that valid titles and descriptions are accepted."""
        task_manager = TaskManager()
        valid_title = "A" * 200  # At the limit
        valid_description = "A" * 1000  # At the limit

        task = task_manager.add_task(valid_title, valid_description)

        assert task.title == valid_title
        assert task.description == valid_description

    def test_update_with_invalid_title(self) -> None:
        """Test that updating with invalid title raises ValidationError."""
        task_manager = TaskManager()
        task = task_manager.add_task("Initial Title")

        with pytest.raises(ValidationError, match="Title cannot be empty."):
            task_manager.update_task(task.id, title="")

    def test_update_with_invalid_description(self) -> None:
        """Test that updating with invalid description raises ValidationError."""
        task_manager = TaskManager()
        task = task_manager.add_task("Initial Title")

        with pytest.raises(ValidationError, match="Description must be 1000 characters or less."):
            task_manager.update_task(task.id, description="A" * 1001)


class TestTaskNotFoundError:
    """Test cases for TaskNotFoundError."""

    def test_get_nonexistent_task(self) -> None:
        """Test that getting a non-existent task raises TaskNotFoundError."""
        task_manager = TaskManager()

        with pytest.raises(TaskNotFoundError, match="Task #1 not found."):
            task_manager.get_task(1)

    def test_update_nonexistent_task(self) -> None:
        """Test that updating a non-existent task raises TaskNotFoundError."""
        task_manager = TaskManager()

        with pytest.raises(TaskNotFoundError, match="Task #1 not found."):
            task_manager.update_task(1, title="New Title")

    def test_delete_nonexistent_task(self) -> None:
        """Test that deleting a non-existent task raises TaskNotFoundError."""
        task_manager = TaskManager()

        with pytest.raises(TaskNotFoundError, match="Task #1 not found."):
            task_manager.delete_task(1)

    def test_complete_nonexistent_task(self) -> None:
        """Test that completing a non-existent task raises TaskNotFoundError."""
        task_manager = TaskManager()

        with pytest.raises(TaskNotFoundError, match="Task #1 not found."):
            task_manager.complete_task(1)