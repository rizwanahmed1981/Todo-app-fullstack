# Data Model: Console Todo App - Phase I

## Task Entity

### Overview
The Task entity represents a single todo item in the console application. It encapsulates all relevant information about a task including its state, metadata, and content.

### Fields

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| id | int | Yes | Unique identifier for the task |
| title | str | Yes | Title of the task (1-200 characters) |
| description | str \| None | No | Detailed description of the task (max 1000 characters) |
| completed | bool | Yes | Boolean indicating if task is complete |
| created_at | datetime | Yes | Timestamp when task was created |
| updated_at | datetime | Yes | Timestamp when task was last updated |

### Validation Rules

1. **Title Validation**:
   - Required field (cannot be empty)
   - Maximum 200 characters
   - Leading/trailing whitespace trimmed

2. **Description Validation**:
   - Optional field (can be None)
   - Maximum 1000 characters if provided

3. **ID Generation**:
   - Automatically generated using auto-increment counter
   - Unique within the session

4. **State Management**:
   - `completed` defaults to `False`
   - `created_at` and `updated_at` automatically populated with current timestamp

### State Transitions

- **Initial State**: `completed = False`, `created_at = now`, `updated_at = now`
- **Completion Toggle**: `completed` flips from `False` to `True` or vice versa
- **Update**: `updated_at` is refreshed on any modification

### Methods

#### `mark_complete()`
- Toggles the `completed` status
- Updates `updated_at` timestamp
- No parameters required

#### `update(title: str | None = None, description: str | None = None)`
- Updates task title and/or description
- Updates `updated_at` timestamp
- Parameters:
  - `title`: New title (optional)
  - `description`: New description (optional)

### Relationships

- **One-to-Many**: One user session can contain many tasks
- **Self-contained**: Tasks do not reference other entities (no foreign keys)

## Custom Exceptions

### TaskNotFoundError
- **Cause**: Attempting to access a task that doesn't exist
- **Trigger**: Invalid task ID in operations like update, delete, complete
- **Message**: "Task #X not found."

### ValidationError
- **Cause**: Invalid input data for task creation or update
- **Trigger**:
  - Empty title
  - Title exceeding 200 characters
  - Description exceeding 1000 characters
- **Messages**:
  - "Title cannot be empty."
  - "Title must be 200 characters or less."
  - "Description must be 1000 characters or less."

## Implementation Details

### Data Storage
- Stored in a Python dictionary: `dict[int, Task]`
- Keys are task IDs
- Values are Task objects

### Persistence Model
- **Session-based**: Data exists only during application lifetime
- **Memory-only**: No external persistence
- **Data Loss**: All data lost when application exits

### Timestamp Handling
- `created_at`: Set once at task creation
- `updated_at`: Updated on any modification or completion toggle
- Both use Python's `datetime.now()` with timezone awareness