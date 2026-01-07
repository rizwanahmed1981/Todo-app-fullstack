'use client';

import { useState } from 'react';
import { useAuth } from '@/lib/auth';
import { createTask } from '@/lib/api';

interface AddTaskFormProps {
  onTaskAdded: (task: any) => void;
}

export function AddTaskForm({ onTaskAdded }: AddTaskFormProps) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const { user } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim() || !user) return;

    setIsLoading(true);

    try {
      const token = localStorage.getItem('authToken');
      if (!token) return;

      const result = await createTask(token, user.id, {
        title: title.trim(),
        description: description.trim() || undefined
      });

      if (result.success && result.data) {
        // Clear form
        setTitle('');
        setDescription('');

        // Notify parent component
        onTaskAdded(result.data);
      }
    } catch (error) {
      console.error('Failed to add task:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="rounded-lg border border-gray-200 bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-800">
      <div className="mb-3">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="What needs to be done?"
          className="w-full rounded border border-gray-300 px-4 py-2 text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
          required
        />
      </div>

      <div className="mb-3">
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Add a description (optional)"
          className="w-full rounded border border-gray-300 px-4 py-2 text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
          rows={2}
        />
      </div>

      <button
        type="submit"
        disabled={isLoading}
        className="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50"
      >
        {isLoading ? 'Adding...' : 'Add Task'}
      </button>
    </form>
  );
}