import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { TaskItem } from '@/components/TaskItem';

describe('TaskItem Component - Error Handling', () => {
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

  it('renders with correct structure for task item', () => {
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

    // Check that all expected elements are present
    expect(screen.getByText(mockTask.title)).toBeInTheDocument();
    expect(screen.getByText(mockTask.description)).toBeInTheDocument();

    // Check checkbox button
    const checkbox = screen.getByRole('button', { name: /Mark as complete/i });
    expect(checkbox).toBeInTheDocument();

    // Check delete button
    const deleteButton = screen.getByRole('button', { name: /Delete task/i });
    expect(deleteButton).toBeInTheDocument();

    // Check edit button
    const editButton = screen.getByRole('button', { name: /Edit task/i });
    expect(editButton).toBeInTheDocument();
  });

  it('applies correct styling for completed tasks', () => {
    const completedTask = {
      ...mockTask,
      completed: true
    };

    render(
      <TaskItem
        id={completedTask.id}
        title={completedTask.title}
        description={completedTask.description}
        completed={completedTask.completed}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
      />
    );

    const titleElement = screen.getByText(completedTask.title);
    expect(titleElement).toHaveClass('line-through');
    expect(titleElement).toHaveClass('text-gray-500');
  });

  it('applies correct styling for incomplete tasks', () => {
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

    const titleElement = screen.getByText(mockTask.title);
    expect(titleElement).not.toHaveClass('line-through');
    expect(titleElement).toHaveClass('text-gray-900');
  });

  it('handles missing description gracefully', () => {
    const taskWithoutDescription = {
      ...mockTask,
      description: undefined
    };

    render(
      <TaskItem
        id={taskWithoutDescription.id}
        title={taskWithoutDescription.title}
        description={taskWithoutDescription.description}
        completed={taskWithoutDescription.completed}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
      />
    );

    // Should not crash when description is undefined
    expect(screen.getByText(taskWithoutDescription.title)).toBeInTheDocument();
  });
});