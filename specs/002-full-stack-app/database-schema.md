# Database Schema

## Overview

This document specifies the database schema for the Phase 2 web application, defining the tables, fields, relationships, and indexes for the Neon Serverless PostgreSQL database.

## Tables

### users (managed by Better Auth)

- id: string (primary key)
- email: string (unique)
- name: string
- created_at: timestamp
- updated_at: timestamp

### tasks

- id: integer (primary key, auto-increment)
- user_id: string (foreign key -> users.id)
- title: string (not null, 1-200 characters)
- description: text (nullable, max 1000 characters)
- completed: boolean (default false)
- created_at: timestamp
- updated_at: timestamp

## Relationships

- tasks.user_id references users.id
- Each task belongs to exactly one user
- Each user can have zero or more tasks

## Indexes

- tasks.user_id (for filtering by user)
- tasks.completed (for status filtering)
- tasks.created_at (for chronological sorting)
- users.email (for user lookup by email)

## Data Integrity

- All foreign key relationships enforced with CASCADE DELETE for tasks when user is deleted
- Timestamps automatically managed by the application
- User_id field always required for task operations
- Title field required for all tasks
- Default values applied for boolean fields

## Security Considerations

- User data is isolated through user_id filtering
- All queries filtered by authenticated user ID
- Database connections use connection pooling
- Access controls configured for proper data isolation

## Performance Considerations

- Indexes created on frequently queried columns
- Proper data types chosen for optimal storage
- Timestamps indexed for efficient sorting and filtering
- Foreign key constraints ensure data consistency