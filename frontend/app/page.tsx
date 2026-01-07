'use client';

import { TaskList } from '../components/TaskList';
import { useState, useEffect } from 'react';

interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  user_id?: string;
}

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        setLoading(true);
        // Using a hardcoded user_id for now as suggested in the instructions
        const response = await fetch('http://localhost:8000/api/user123/tasks');

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setTasks(data);
        setError(null);
      } catch (err) {
        console.error('Failed to fetch tasks:', err);
        setError('Failed to load tasks. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);

  const handleToggleComplete = async (id: number) => {
    try {
      // Optimistically update UI
      setTasks(tasks.map(task =>
        task.id === id ? { ...task, completed: !task.completed } : task
      ));

      // Send update to backend
      const response = await fetch(`http://localhost:8000/api/user123/tasks/${id}/complete`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Refresh tasks from backend to ensure consistency
      const refreshedResponse = await fetch('http://localhost:8000/api/user123/tasks');
      if (refreshedResponse.ok) {
        const refreshedData = await refreshedResponse.json();
        setTasks(refreshedData);
      }
    } catch (err) {
      console.error('Failed to update task completion:', err);
      // Revert optimistic update on error
      setTasks(tasks.map(task =>
        task.id === id ? { ...task, completed: !task.completed } : task
      ));
      setError('Failed to update task. Please try again.');
    }
  };

  const handleDelete = async (id: number) => {
    try {
      // Optimistically update UI
      setTasks(tasks.filter(task => task.id !== id));

      // Send delete request to backend
      const response = await fetch(`http://localhost:8000/api/user123/tasks/${id}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    } catch (err) {
      console.error('Failed to delete task:', err);
      // Revert optimistic update on error
      // Note: We can't easily restore the deleted task, but we could show a notification
      setError('Failed to delete task. Please try again.');
    }
  };

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
        <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-16 px-4 bg-white dark:bg-black sm:items-start">
          <div className="w-full">
            <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Todo App</h1>
            <div className="mb-8">
              <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">Your Tasks</h2>
              <div className="rounded-lg border border-gray-200 bg-white p-8 text-center shadow-sm dark:border-gray-700 dark:bg-gray-800">
                <p className="text-gray-500 dark:text-gray-400">Loading tasks...</p>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
        <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-16 px-4 bg-white dark:bg-black sm:items-start">
          <div className="w-full">
            <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Todo App</h1>
            <div className="mb-8">
              <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">Your Tasks</h2>
              <div className="rounded-lg border border-red-200 bg-red-50 p-8 text-center shadow-sm dark:border-red-800 dark:bg-red-900/20">
                <p className="text-red-700 dark:text-red-300">{error}</p>
                <button
                  onClick={() => window.location.reload()}
                  className="mt-4 rounded bg-red-600 px-4 py-2 text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                >
                  Retry
                </button>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-16 px-4 bg-white dark:bg-black sm:items-start">
        <div className="w-full">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Todo App</h1>

          <div className="mb-8">
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">Your Tasks</h2>
            <TaskList
              tasks={tasks}
              onToggleComplete={handleToggleComplete}
              onDelete={handleDelete}
            />
          </div>

          <div className="mt-8">
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">Add New Task</h2>
            <div className="rounded-lg border border-gray-200 bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-800">
              <input
                type="text"
                placeholder="What needs to be done?"
                className="w-full rounded border border-gray-300 px-4 py-2 text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
              />
              <button className="mt-2 rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                Add Task
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
