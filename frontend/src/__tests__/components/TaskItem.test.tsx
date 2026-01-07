import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { TaskItem } from '@/components/TaskItem';

describe('TaskItem Component', () => {
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

  it('renders the task title correctly', () => {
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

    expect(screen.getByText(mockTask.title)).toBeInTheDocument();
  });

  it('renders the task description correctly', () => {
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

    expect(screen.getByText(mockTask.description)).toBeInTheDocument();
  });

  it('renders completed task with strikethrough and dimmed text', () => {
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

  it('renders incomplete task with normal text styling', () => {
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

  it('calls onToggleComplete when checkbox is clicked', () => {
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
    fireEvent.click(checkbox);

    expect(mockOnToggleComplete).toHaveBeenCalledTimes(1);
    expect(mockOnToggleComplete).toHaveBeenCalledWith(mockTask.id);
  });

  it('calls onDelete when delete button is clicked', () => {
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
    fireEvent.click(deleteButton);

    expect(mockOnDelete).toHaveBeenCalledTimes(1);
    expect(mockOnDelete).toHaveBeenCalledWith(mockTask.id);
  });

  it('renders checkbox correctly for incomplete task', () => {
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
    expect(checkbox).toHaveClass('border-gray-300');
    expect(checkbox).not.toHaveClass('border-green-500');
    expect(checkbox).not.toHaveClass('bg-green-500');
    expect(checkbox).not.toHaveClass('text-white');
  });

  it('renders checkbox correctly for completed task', () => {
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

    const checkbox = screen.getByRole('button', { name: /Mark as incomplete/i });
    expect(checkbox).toHaveClass('border-green-500');
    expect(checkbox).toHaveClass('bg-green-500');
    expect(checkbox).toHaveClass('text-white');
  });

  it('renders delete button with proper icon', () => {
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
    expect(deleteButton).toBeInTheDocument();

    // Check that the delete icon is present
    const deleteIcon = screen.getByRole('img', { hidden: true });
    expect(deleteIcon).toBeInTheDocument();
  });
});