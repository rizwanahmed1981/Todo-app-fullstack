"""Unit tests for the task manager module.

This module tests the TaskManager class and its methods.
"""
import pytest
from datetime import datetime

from src.models import Task, TaskNotFoundError, ValidationError
from src.task_manager import TaskManager


class TestTaskManager:
    """Test cases for the TaskManager class."""

    def test_add_task(self) -> None:
        """Test adding a task."""
        task_manager = TaskManager()

        task = task_manager.add_task("Test Title", "Test Description")

        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description == "Test Description"
        assert task.completed is False
        assert task.created_at is not None
        assert task.updated_at is not None

    def test_add_task_optional_description(self) -> None:
        """Test adding a task with optional description omitted."""
        task_manager = TaskManager()

        task = task_manager.add_task("Test Title")

        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description is None
        assert task.completed is False

    def test_add_multiple_tasks(self) -> None:
        """Test adding multiple tasks with unique IDs."""
        task_manager = TaskManager()

        task1 = task_manager.add_task("Task 1")
        task2 = task_manager.add_task("Task 2")
        task3 = task_manager.add_task("Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_list_tasks_empty(self) -> None:
        """Test listing tasks when no tasks exist."""
        task_manager = TaskManager()

        tasks = task_manager.list_tasks()

        assert tasks == []

    def test_list_tasks_with_tasks(self) -> None:
        """Test listing tasks when tasks exist."""
        task_manager = TaskManager()

        task1 = task_manager.add_task("Task 1")
        task2 = task_manager.add_task("Task 2")
        task3 = task_manager.add_task("Task 3")

        tasks = task_manager.list_tasks()

        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3

    def test_get_task(self) -> None:
        """Test getting a specific task."""
        task_manager = TaskManager()
        original_task = task_manager.add_task("Test Title", "Test Description")

        retrieved_task = task_manager.get_task(original_task.id)

        assert retrieved_task.id == original_task.id
        assert retrieved_task.title == original_task.title
        assert retrieved_task.description == original_task.description
        assert retrieved_task.completed == original_task.completed

    def test_update_task_title(self) -> None:
        """Test updating a task's title."""
        task_manager = TaskManager()
        original_task = task_manager.add_task("Original Title", "Original Description")

        updated_task = task_manager.update_task(original_task.id, title="New Title")

        assert updated_task.id == original_task.id
        assert updated_task.title == "New Title"
        assert updated_task.description == "Original Description"
        assert updated_task.completed == original_task.completed

    def test_update_task_description(self) -> None:
        """Test updating a task's description."""
        task_manager = TaskManager()
        original_task = task_manager.add_task("Original Title", "Original Description")

        updated_task = task_manager.update_task(original_task.id, description="New Description")

        assert updated_task.id == original_task.id
        assert updated_task.title == "Original Title"
        assert updated_task.description == "New Description"
        assert updated_task.completed == original_task.completed

    def test_update_task_both(self) -> None:
        """Test updating both title and description."""
        task_manager = TaskManager()
        original_task = task_manager.add_task("Original Title", "Original Description")

        updated_task = task_manager.update_task(
            original_task.id,
            title="New Title",
            description="New Description"
        )

        assert updated_task.id == original_task.id
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"
        assert updated_task.completed == original_task.completed

    def test_update_task_partial(self) -> None:
        """Test updating only one field leaves the other unchanged."""
        task_manager = TaskManager()
        original_task = task_manager.add_task("Original Title", "Original Description")

        # Update only title
        updated_task = task_manager.update_task(original_task.id, title="New Title")

        assert updated_task.title == "New Title"
        assert updated_task.description == "Original Description"

        # Update only description
        updated_task2 = task_manager.update_task(updated_task.id, description="New Description")

        assert updated_task2.title == "New Title"
        assert updated_task2.description == "New Description"

    def test_delete_task(self) -> None:
        """Test deleting a task."""
        task_manager = TaskManager()
        task = task_manager.add_task("Test Title")

        deleted_task = task_manager.delete_task(task.id)

        assert deleted_task.id == task.id
        assert deleted_task.title == task.title

        # Verify task is no longer in the manager
        with pytest.raises(TaskNotFoundError):
            task_manager.get_task(task.id)

    def test_complete_task(self) -> None:
        """Test completing a task."""
        task_manager = TaskManager()
        task = task_manager.add_task("Test Title")

        # Initially incomplete
        assert task.completed is False

        # Complete the task
        completed_task = task_manager.complete_task(task.id)
        assert completed_task.completed is True

        # Verify the change is persisted
        retrieved_task = task_manager.get_task(task.id)
        assert retrieved_task.completed is True

    def test_toggle_task_completion(self) -> None:
        """Test toggling a task's completion status."""
        task_manager = TaskManager()
        task = task_manager.add_task("Test Title")

        # Initially incomplete
        assert task.completed is False

        # Complete the task
        task_manager.complete_task(task.id)
        retrieved_task1 = task_manager.get_task(task.id)
        assert retrieved_task1.completed is True

        # Incomplete the task again
        task_manager.complete_task(task.id)
        retrieved_task2 = task_manager.get_task(task.id)
        assert retrieved_task2.completed is False

    def test_task_timestamps(self) -> None:
        """Test that timestamps are properly set and updated."""
        task_manager = TaskManager()

        # Add a task
        task = task_manager.add_task("Test Title")
        initial_created = task.created_at
        initial_updated = task.updated_at

        # Update the task
        task_manager.update_task(task.id, title="Updated Title")
        updated_task = task_manager.get_task(task.id)

        # Verify created_at is unchanged
        assert updated_task.created_at == initial_created

        # Verify updated_at is changed
        assert updated_task.updated_at > initial_updated

    def test_task_title_trimming(self) -> None:
        """Test that task titles are properly trimmed."""
        task_manager = TaskManager()

        task = task_manager.add_task("  Spaced Title  ", "  Spaced Description  ")

        assert task.title == "Spaced Title"
        # Description should remain as provided (not trimmed)
        assert task.description == "  Spaced Description  "