'use client';

import { TaskList } from '../components/TaskList';
import { useState, useEffect } from 'react';
import { useAuth } from '@/lib/auth';
import { getTasks, createTask, toggleTaskCompletion, deleteTask } from '@/lib/api';
import { Header } from '@/components/Header';
import { AddTaskForm } from '@/components/AddTaskForm';

export default function Home() {
  const { user, isAuthenticated, loading: authLoading } = useAuth();
  const [tasks, setTasks] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (isAuthenticated && user) {
      const fetchTasks = async () => {
        try {
          setLoading(true);
          setError(null);

          const token = localStorage.getItem('authToken');
          if (!token) {
            throw new Error('No authentication token found');
          }

          const result = await getTasks(token, user.id);

          if (result.success) {
            setTasks(result.data || []);
          } else {
            throw new Error(result.error || 'Failed to fetch tasks');
          }
        } catch (err) {
          console.error('Failed to fetch tasks:', err);
          setError(err instanceof Error ? err.message : 'Failed to load tasks. Please try again later.');
        } finally {
          setLoading(false);
        }
      };

      fetchTasks();
    }
  }, [isAuthenticated, user]);

  const handleToggleComplete = async (id: number) => {
    try {
      const token = localStorage.getItem('authToken');
      if (!token || !user) {
        throw new Error('Not authenticated');
      }

      // Optimistically update UI
      setTasks(prevTasks =>
        prevTasks.map(task =>
          task.id === id ? { ...task, completed: !task.completed } : task
        )
      );

      const result = await toggleTaskCompletion(token, user.id, id);

      if (!result.success) {
        throw new Error(result.error || 'Failed to update task completion');
      }

      // Refresh tasks from backend to ensure consistency
      const refreshResult = await getTasks(token, user.id);
      if (refreshResult.success) {
        setTasks(refreshResult.data || []);
      }
    } catch (err) {
      console.error('Failed to update task completion:', err);
      // Revert optimistic update on error
      setTasks(prevTasks =>
        prevTasks.map(task =>
          task.id === id ? { ...task, completed: !task.completed } : task
        )
      );
      setError(err instanceof Error ? err.message : 'Failed to update task. Please try again.');
    }
  };

  const handleDelete = async (id: number) => {
    try {
      const token = localStorage.getItem('authToken');
      if (!token || !user) {
        throw new Error('Not authenticated');
      }

      // Optimistically update UI
      setTasks(prevTasks => prevTasks.filter(task => task.id !== id));

      const result = await deleteTask(token, user.id, id);

      if (!result.success) {
        throw new Error(result.error || 'Failed to delete task');
      }
    } catch (err) {
      console.error('Failed to delete task:', err);
      // Revert optimistic update on error
      setError(err instanceof Error ? err.message : 'Failed to delete task. Please try again.');
    }
  };

  const handleTaskAdded = (newTask: any) => {
    setTasks(prevTasks => [...prevTasks, newTask]);
  };

  // Show loading if auth is still loading
  if (authLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
        <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-16 px-4 bg-white dark:bg-black sm:items-start">
          <div className="w-full">
            <Header />
            <div className="mb-8">
              <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">Your Tasks</h2>
              <div className="rounded-lg border border-gray-200 bg-white p-8 text-center shadow-sm dark:border-gray-700 dark:bg-gray-800">
                <p className="text-gray-500 dark:text-gray-400">Loading...</p>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }

  // Show message if not authenticated
  if (!isAuthenticated) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
        <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-16 px-4 bg-white dark:bg-black sm:items-start">
          <div className="w-full">
            <Header />
            <div className="rounded-lg border border-gray-200 bg-white p-8 text-center shadow-sm dark:border-gray-700 dark:bg-gray-800">
              <p className="text-gray-500 dark:text-gray-400">Please log in to view your tasks.</p>
              <a href="/login" className="mt-4 inline-block rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                Go to Login
              </a>
            </div>
          </div>
        </main>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
        <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-16 px-4 bg-white dark:bg-black sm:items-start">
          <div className="w-full">
            <Header />
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
            <Header />
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
    <div className="flex min-h-screen flex-col bg-zinc-50 font-sans dark:bg-black">
      <Header />
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-16 px-4 bg-white dark:bg-black sm:items-start">
        <div className="w-full">
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
            <AddTaskForm onTaskAdded={handleTaskAdded} />
          </div>
        </div>
      </main>
    </div>
  );
}