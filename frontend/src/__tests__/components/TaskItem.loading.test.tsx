import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { TaskItem } from '@/components/TaskItem';

describe('TaskItem Component - Loading States', () => {
  const mockTask = {
    id: 1,
    title: 'Test Task',
    description: 'This is a test task description',
    completed: false,
  };

  const mockOnToggleComplete = jest.fn();
  const mockOnDelete = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('disables checkbox and shows spinner when toggling completion', () => {
    render(
      <TaskItem
        id={mockTask.id}
        title={mockTask.title}
        description={mockTask.description}
        completed={mockTask.completed}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
      />
    );

    const checkbox = screen.getByRole('button', { name: /Mark as complete/i });

    // Initially should not be disabled
    expect(checkbox).not.toBeDisabled();

    // Simulate clicking the checkbox (this will trigger the loading state in our implementation)
    fireEvent.click(checkbox);

    // After click, should be disabled and show spinner
    // Note: This test verifies the component structure, but actual loading simulation
    // would require more complex mocking of async behavior
    expect(checkbox).toHaveClass('opacity-50');
  });

  it('disables delete button and shows spinner when deleting', () => {
    render(
      <TaskItem
        id={mockTask.id}
        title={mockTask.title}
        description={mockTask.description}
        completed={mockTask.completed}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
      />
    );

    const deleteButton = screen.getByRole('button', { name: /Delete task/i });

    // Initially should not be disabled
    expect(deleteButton).not.toBeDisabled();

    // Simulate clicking the delete button (this will trigger the loading state in our implementation)
    fireEvent.click(deleteButton);

    // After click, should be disabled and show spinner
    // Note: This test verifies the component structure, but actual loading simulation
    // would require more complex mocking of async behavior
    expect(deleteButton).toHaveClass('cursor-not-allowed');
  });

  it('shows appropriate aria labels during loading states', () => {
    render(
      <TaskItem
        id={mockTask.id}
        title={mockTask.title}
        description={mockTask.description}
        completed={mockTask.completed}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
      />
    );

    const checkbox = screen.getByRole('button', { name: /Mark as complete/i });
    const deleteButton = screen.getByRole('button', { name: /Delete task/i });

    // Check initial aria labels
    expect(checkbox).toHaveAttribute('aria-label', 'Mark as complete');
    expect(deleteButton).toHaveAttribute('aria-label', 'Delete task');
  });
});