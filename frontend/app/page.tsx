'use client';

import { TaskList } from '../components/TaskList';
import { useState } from 'react';

export default function Home() {
  // Sample tasks for demonstration
  const [tasks, setTasks] = useState([
    {
      id: 1,
      title: "Create project structure",
      description: "Set up the basic directory structure and configuration files",
      completed: true
    },
    {
      id: 2,
      title: "Implement task management features",
      description: "Add ability to create, read, update, and delete tasks",
      completed: false
    },
    {
      id: 3,
      title: "Style task items",
      description: "Apply modern styling to task cards with hover effects",
      completed: false
    }
  ]);

  const handleToggleComplete = (id: number) => {
    setTasks(tasks.map(task =>
      task.id === id ? { ...task, completed: !task.completed } : task
    ));
  };

  const handleDelete = (id: number) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

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
