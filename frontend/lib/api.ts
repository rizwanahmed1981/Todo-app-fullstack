// API client for authentication and other API calls
import { API_BASE_URL } from '@/lib/constants';

// Define types for authentication responses
export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  token: string;
  user: {
    id: string;
    email: string;
    name?: string;
  };
}

export interface SignupRequest {
  email: string;
  password: string;
  name?: string;
}

export interface SignupResponse {
  token: string;
  user: {
    id: string;
    email: string;
    name?: string;
  };
}

export interface AuthErrorResponse {
  message: string;
  error?: string;
}

/**
 * Send login request to backend
 */
export async function login(credentials: LoginRequest): Promise<{ success: boolean; data?: LoginResponse; error?: string }> {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });

    if (!response.ok) {
      const errorData: AuthErrorResponse = await response.json();
      return {
        success: false,
        error: errorData.message || 'Login failed'
      };
    }

    const data: LoginResponse = await response.json();
    return {
      success: true,
      data
    };
  } catch (error) {
    console.error('Login error:', error);
    return {
      success: false,
      error: 'Network error. Please try again.'
    };
  }
}

/**
 * Send signup request to backend
 */
export async function signup(userData: SignupRequest): Promise<{ success: boolean; data?: SignupResponse; error?: string }> {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/signup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      const errorData: AuthErrorResponse = await response.json();
      return {
        success: false,
        error: errorData.message || 'Signup failed'
      };
    }

    const data: SignupResponse = await response.json();
    return {
      success: true,
      data
    };
  } catch (error) {
    console.error('Signup error:', error);
    return {
      success: false,
      error: 'Network error. Please try again.'
    };
  }
}

/**
 * Get user profile (requires authentication)
 */
export async function getUserProfile(token: string): Promise<{ success: boolean; data?: any; error?: string }> {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/profile`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const errorData: AuthErrorResponse = await response.json();
      return {
        success: false,
        error: errorData.message || 'Failed to fetch user profile'
      };
    }

    const data = await response.json();
    return {
      success: true,
      data
    };
  } catch (error) {
    console.error('Get user profile error:', error);
    return {
      success: false,
      error: 'Network error. Please try again.'
    };
  }
}

/**
 * Logout user (clears token)
 */
export async function logout(): Promise<{ success: boolean; error?: string }> {
  try {
    // In a real app, you might want to call a logout endpoint to invalidate the token on the server
    // For now, we'll just clear the local storage/session

    // Clear any stored tokens or session data
    localStorage.removeItem('authToken');
    document.cookie = 'authToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';

    return {
      success: true
    };
  } catch (error) {
    console.error('Logout error:', error);
    return {
      success: false,
      error: 'Failed to logout'
    };
  }
}