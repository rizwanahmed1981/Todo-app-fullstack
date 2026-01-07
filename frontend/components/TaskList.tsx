'use client';

import React, { useState } from 'react';
import { TaskItem } from './TaskItem';
import { EditTaskModal } from './EditTaskModal';

export interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  user_id?: string;
  created_at?: string;
  updated_at?: string;
}

interface TaskListProps {
  tasks: Task[];
  onToggleComplete?: (id: number) => void;
  onDelete?: (id: number) => void;
}

export const TaskList: React.FC<TaskListProps> = ({ tasks, onToggleComplete, onDelete }) => {
  const [editingTask, setEditingTask] = useState<any>(null);

  const handleEdit = (task: any) => {
    setEditingTask(task);
  };

  const handleSaveEdit = (updatedTask: any) => {
    // In a real app, you'd update the task in the parent component
    // For now, we'll just close the modal
    setEditingTask(null);
  };

  const handleCancelEdit = () => {
    setEditingTask(null);
  };

  if (tasks.length === 0) {
    return (
      <div className="rounded-lg border border-gray-200 bg-white p-8 text-center shadow-sm dark:border-gray-700 dark:bg-gray-800">
        <p className="text-gray-500 dark:text-gray-400">No tasks yet. Add some tasks to get started!</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          id={task.id}
          title={task.title}
          description={task.description}
          completed={task.completed}
          onToggleComplete={onToggleComplete}
          onDelete={onDelete}
          onEdit={() => handleEdit(task)}
        />
      ))}

      {editingTask && (
        <EditTaskModal
          task={editingTask}
          onSave={handleSaveEdit}
          onCancel={handleCancelEdit}
        />
      )}
    </div>
  );
};