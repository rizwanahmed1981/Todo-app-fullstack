'use client';

import React, { useState } from 'react';

interface TaskItemProps {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  onToggleComplete?: (id: number) => void;
  onDelete?: (id: number) => void;
  onEdit?: (id: number) => void;
}

export const TaskItem: React.FC<TaskItemProps> = ({
  id,
  title,
  description,
  completed,
  onToggleComplete,
  onDelete,
  onEdit
}) => {
  const [isToggling, setIsToggling] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);

  const handleToggleComplete = async () => {
    if (onToggleComplete && !isToggling) {
      setIsToggling(true);
      try {
        await onToggleComplete(id);
      } finally {
        setIsToggling(false);
      }
    }
  };

  const handleDelete = async () => {
    if (onDelete && !isDeleting) {
      setIsDeleting(true);
      try {
        await onDelete(id);
      } finally {
        setIsDeleting(false);
      }
    }
  };

  return (
    <div
      className={`rounded-lg border border-gray-200 bg-white p-4 shadow-sm transition-all duration-200 hover:shadow-md dark:border-gray-700 dark:bg-gray-800 ${
        completed ? 'opacity-75' : ''
      }`}
    >
      <div className="flex items-start justify-between">
        <div className="flex items-start space-x-3">
          <button
            onClick={handleToggleComplete}
            disabled={isToggling}
            className={`mt-1 flex h-5 w-5 items-center justify-center rounded-full border-2 ${
              completed
                ? 'border-green-500 bg-green-500 text-white'
                : 'border-gray-300 hover:border-green-400 dark:border-gray-600 dark:hover:border-green-400'
            } ${isToggling ? 'opacity-50 cursor-not-allowed' : ''}`}
            aria-label={isToggling ? "Updating..." : (completed ? "Mark as incomplete" : "Mark as complete")}
          >
            {isToggling ? (
              <svg className="h-3 w-3 animate-spin text-current" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            ) : completed && (
              <svg className="h-3 w-3" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
            )}
          </button>
          <div>
            <h3 className={`text-lg font-semibold ${completed ? 'line-through text-gray-500' : 'text-gray-900 dark:text-white'}`}>
              {title}
            </h3>
            {description && (
              <p className="mt-1 text-sm text-gray-600 dark:text-gray-400">
                {description}
              </p>
            )}
          </div>
        </div>
        <div className="flex space-x-2">
          <button
            onClick={() => onEdit?.(id)}
            className="rounded-md p-1 text-gray-400 hover:text-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
            aria-label="Edit task"
          >
            <svg className="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
            </svg>
          </button>
          <button
            onClick={handleDelete}
            disabled={isDeleting}
            className={`rounded-md p-1 ${isDeleting ? 'text-gray-300' : 'text-gray-400 hover:text-red-500'} focus:outline-none focus:ring-2 focus:ring-red-500 ${isDeleting ? 'cursor-not-allowed' : ''}`}
            aria-label={isDeleting ? "Deleting..." : "Delete task"}
          >
            {isDeleting ? (
              <svg className="h-5 w-5 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            ) : (
              <svg className="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};