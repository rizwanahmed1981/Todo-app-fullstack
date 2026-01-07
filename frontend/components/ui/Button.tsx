'use client';

import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary';
  fullWidth?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  fullWidth = false,
  ...props
}) => {
  const baseClasses = 'rounded-md px-4 py-2 text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2';

  const variantClasses = variant === 'primary'
    ? 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500'
    : 'bg-white text-gray-700 hover:bg-gray-50 focus:ring-gray-500 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600 dark:focus:ring-gray-500';

  const widthClasses = fullWidth ? 'w-full' : '';

  return (
    <button
      className={`${baseClasses} ${variantClasses} ${widthClasses}`}
      {...props}
    >
      {children}
    </button>
  );
};