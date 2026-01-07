// Authentication context and utilities
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { login, signup, logout, getUserProfile } from '@/lib/api';

// Define types
export interface User {
  id: string;
  email: string;
  name?: string;
}

export interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<{ success: boolean; error?: string }>;
  signup: (email: string, password: string, name?: string) => Promise<{ success: boolean; error?: string }>;
  logout: () => Promise<void>;
  loading: boolean;
}

// Create context
export const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Provider component
export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // Check if user is already authenticated on mount
  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        // Try to get token from localStorage or cookies
        const token = localStorage.getItem('authToken') || getCookie('authToken');

        if (token) {
          // Verify token with backend
          const profileResult = await getUserProfile(token);
          if (profileResult.success && profileResult.data) {
            setUser(profileResult.data);
          } else {
            // Token is invalid, clear it
            localStorage.removeItem('authToken');
            document.cookie = 'authToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
          }
        }
      } catch (error) {
        console.error('Error checking auth status:', error);
        // Clear any potentially invalid token
        localStorage.removeItem('authToken');
        document.cookie = 'authToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
      } finally {
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  // Helper function to get cookie value
  const getCookie = (name: string): string | null => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop()?.split(';').shift() || null;
    return null;
  };

  // Login function
  const handleLogin = async (email: string, password: string) => {
    try {
      const result = await login({ email, password });

      if (result.success && result.data) {
        // Store token
        localStorage.setItem('authToken', result.data.token);

        // Set user data
        setUser(result.data.user);

        return { success: true };
      } else {
        return {
          success: false,
          error: result.error || 'Login failed'
        };
      }
    } catch (error) {
      console.error('Login error:', error);
      return {
        success: false,
        error: 'An unexpected error occurred'
      };
    }
  };

  // Signup function
  const handleSignup = async (email: string, password: string, name?: string) => {
    try {
      const result = await signup({ email, password, name });

      if (result.success && result.data) {
        // Store token
        localStorage.setItem('authToken', result.data.token);

        // Set user data
        setUser(result.data.user);

        return { success: true };
      } else {
        return {
          success: false,
          error: result.error || 'Signup failed'
        };
      }
    } catch (error) {
      console.error('Signup error:', error);
      return {
        success: false,
        error: 'An unexpected error occurred'
      };
    }
  };

  // Logout function
  const handleLogout = async () => {
    try {
      await logout();
      setUser(null);
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  const value = {
    user,
    isAuthenticated: !!user,
    login: handleLogin,
    signup: handleSignup,
    logout: handleLogout,
    loading
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use auth context
export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};