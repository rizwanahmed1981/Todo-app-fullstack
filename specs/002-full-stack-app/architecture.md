# Architecture: Full-Stack Web Application

## Overview

This document describes the architecture for the Phase 2 full-stack web application, which transforms the console app into a multi-user web application with authentication and persistent storage.

## Monorepo Structure

The project follows a monorepo structure with the following key directories:

- `/frontend` - Next.js 16 application with App Router
- `/backend` - FastAPI Python backend service
- `/specs/002-full-stack-app/` - Specification files for this phase

## System Components

### Frontend Layer (Next.js 16)

The frontend is built using Next.js 16 with App Router, implementing:
- Server Components by default for better performance
- Client Components only for interactivity
- TypeScript for type safety
- Tailwind CSS for styling
- Better Auth integration for user sessions

### Backend Layer (FastAPI)

The backend is implemented with FastAPI and follows these principles:
- RESTful API design with async/await patterns
- SQLModel ORM for database operations
- JWT-based authentication with Better Auth
- All API endpoints secured with proper authentication

### Database Layer (Neon Serverless PostgreSQL)

The database uses Neon Serverless PostgreSQL for:
- User data storage (managed by Better Auth)
- Task data storage with proper indexing
- Connection pooling for performance
- Data isolation between users

## Communication Flow

1. **User Authentication Flow**:
   - User accesses frontend and initiates login/signup via Better Auth
   - Better Auth creates JWT tokens for authenticated sessions
   - Frontend stores and includes JWT tokens in all subsequent API requests

2. **API Communication**:
   - Frontend makes REST API calls to backend using `/api/{user_id}/` endpoints
   - All API requests include JWT token in Authorization header
   - Backend validates JWT tokens and filters data by authenticated user ID
   - Backend communicates with database using SQLModel ORM

3. **Data Flow**:
   - User actions in frontend trigger API calls to backend
   - Backend validates authentication and processes requests
   - Backend stores/retrieves data from Neon PostgreSQL
   - Responses are returned to frontend for UI updates

## Security Considerations

- All API endpoints require valid JWT tokens
- User data is isolated through user_id filtering
- Tokens are transmitted securely over HTTPS
- Input validation and sanitization applied to all user inputs
- SQL injection prevention through ORM usage
- XSS protection through proper output encoding

## Scalability Considerations

- Stateless service design enabling horizontal scaling
- Database connection pooling for efficient resource utilization
- Proper indexing for database query optimization
- Caching strategies for frequently accessed data
- Load balancing preparation for future scaling needs