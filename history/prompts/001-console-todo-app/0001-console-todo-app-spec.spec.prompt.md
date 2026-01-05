---
id: 0001
title: console-todo-app-spec
created: 2026-01-05
stage: spec
feature: 001-console-todo-app
tags: [specification, console-app, todo-app]
status: completed
---

# Console Todo App - Phase I Specification

## Original Prompt

You are creating detailed specifications for Phase I: In-Memory Python Console Todo App.

## Context
- Phase: Phase I (Console Application)
- Due: December 7, 2025
- Points: 100
- Tech Stack: Python 3.14, UV package manager
- Storage: In-memory (no database)
- Features: Basic Level (5 core features)

## Generate a Specification Document (speckit.specify) that includes:

### 1. Project Overview
- Name: Todo Console App - Phase I
- Purpose: Command-line todo manager with in-memory storage
- Success Criteria: All 5 basic features working via CLI
- Constraints: No manual coding (Claude Code + Spec-Kit only)

### 2. User Journeys
Create detailed user journeys for:

**Journey 1: First-Time User**
- User starts the application
- User sees a welcome message and menu
- User explores available commands
- User adds their first task
- User views the task list
- User exits the application

**Journey 2: Power User**
- User starts application
- User adds multiple tasks
- User views all tasks
- User updates a task description
- User marks a task complete
- User deletes completed tasks
- User exits

**Journey 3: Error Recovery**
- User enters invalid command
- User tries to delete non-existent task
- User tries to update non-existent task
- Application handles errors gracefully

### 3. Feature Requirements

#### FR-001: Add Task
**Description**: User can create a new todo task with title and optional description.

**User Story**: As a user, I want to add a new task so that I can track things I need to do.

**Acceptance Criteria**:
- ✅ User can enter task title (required, 1-200 characters)
- ✅ User can enter task description (optional, max 1000 characters)
- ✅ System generates unique task ID automatically
- ✅ Task is marked as incomplete by default
- ✅ Task is stored in memory
- ✅ System confirms task creation with ID
- ❌ Empty title is rejected with error message
- ❌ Title over 200 characters is rejected

**Input/Output**:
Input:
Command: add
Title: "Buy groceries"
Description: "Milk, eggs, bread"
Output:
"✓ Task #1 created: Buy groceries"

#### FR-002: View Task List
**Description**: User can view all tasks with their status and details.

**User Story**: As a user, I want to see all my tasks so that I know what I need to do.

**Acceptance Criteria**:
- ✅ Display all tasks with ID, title, and status
- ✅ Show completion status (✓ complete, ○ incomplete)
- ✅ Display in creation order (oldest first)
- ✅ Show task count summary
- ✅ Handle empty list gracefully
- ✅ Show description if available

**Input/Output**:
Input: list
Output:
Your Tasks (3 total, 1 complete):
○ [1] Buy groceries - Milk, eggs, bread
✓ [2] Call mom
○ [3] Finish report

#### FR-003: Update Task
**Description**: User can modify task title and/or description.

**User Story**: As a user, I want to update task details so that I can correct mistakes or add information.

**Acceptance Criteria**:
- ✅ User can update title by task ID
- ✅ User can update description by task ID
- ✅ User can update both simultaneously
- ✅ System confirms update
- ❌ Invalid task ID shows error
- ✅ Validation rules same as creation

**Input/Output**:
Input:
Command: update
Task ID: 1
New Title: "Buy groceries and fruits"
Output:
"✓ Task #1 updated"

#### FR-004: Delete Task
**Description**: User can remove tasks from the list.

**User Story**: As a user, I want to delete tasks so that I can remove items I no longer need.

**Acceptance Criteria**:
- ✅ User can delete task by ID
- ✅ Task is removed from memory
- ✅ System confirms deletion
- ❌ Invalid task ID shows error
- ✅ Confirmation prompt before deletion (optional)

**Input/Output**:
Input:
Command: delete
Task ID: 2
Output:
"✓ Task #2 deleted: Call mom"

#### FR-005: Mark Complete/Incomplete
**Description**: User can toggle task completion status.

**User Story**: As a user, I want to mark tasks as complete so that I can track my progress.

**Acceptance Criteria**:
- ✅ User can mark task complete by ID
- ✅ User can mark task incomplete by ID (toggle)
- ✅ Status changes reflected in list view
- ✅ System confirms status change
- ❌ Invalid task ID shows error

**Input/Output**:
Input:
Command: complete
Task ID: 1
Output:
"✓ Task #1 marked as complete: Buy groceries"

### 4. Non-Functional Requirements

#### NFR-001: Performance
- Application starts in < 1 second
- All operations complete in < 100ms
- Memory usage < 50MB

#### NFR-002: Usability
- Clear command menu always visible
- Helpful error messages
- Intuitive command syntax
- Color-coded output (optional)

#### NFR-003: Code Quality
- 100% type hints coverage
- All functions have docstrings
- PEP 8 compliant
- No code duplication
- Modular design

#### NFR-004: Testing
- Unit tests for all CRUD operations
- Test edge cases (empty lists, invalid IDs)
- Test input validation
- 80%+ code coverage

### 5. Data Models
```python
@dataclass
class Task:
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    updated_at: datetime
```

### 6. User Interface Specification

**Command Structure**:
- `add` - Add new task
- `list` - View all tasks
- `update <id>` - Update task
- `delete <id>` - Delete task
- `complete <id>` - Toggle completion
- `help` - Show help
- `exit` - Exit application

**Menu Format**:
╔════════════════════════════════╗
║     TODO CONSOLE APP v1.0      ║
╠════════════════════════════════╣
║  Commands:                     ║
║  add     - Add new task        ║
║  list    - View all tasks      ║
║  update  - Update task         ║
║  delete  - Remove task         ║
║  complete- Mark complete       ║
║  help    - Show this menu      ║
║  exit    - Exit application    ║
╚════════════════════════════════╝

### 7. Error Handling

Define error scenarios:
- Invalid command: "Unknown command. Type 'help' for options."
- Invalid task ID: "Task #X not found."
- Empty title: "Title cannot be empty."
- Title too long: "Title must be 200 characters or less."
- No tasks: "No tasks found. Use 'add' to create one."

### 8. Validation Rules

- Title: Required, 1-200 characters, non-empty after trim
- Description: Optional, max 1000 characters
- Task ID: Must exist in current task list
- Commands: Must match defined command list

### 9. Dependencies

List required packages (via UV):
- No external dependencies for core functionality
- Optional: `rich` for colored terminal output
- Development: `pytest` for testing

### 10. Success Metrics

Phase I is complete when:
- ✅ All 5 basic features work correctly
- ✅ All acceptance criteria met
- ✅ Tests pass with 80%+ coverage
- ✅ Code follows constitution principles
- ✅ README has setup instructions
- ✅ Demo video recorded (< 90 seconds)

## Output Format
Create `speckit.specify` as a markdown document with all sections above.

## Response Summary

Successfully created detailed specifications for Phase I: In-Memory Python Console Todo App with all required sections including:
- Project overview
- User journeys
- Feature requirements (FR-001 through FR-005)
- Non-functional requirements
- Data models
- User interface specification
- Error handling scenarios
- Validation rules
- Dependencies
- Success metrics

Created both the detailed spec.md file in specs/001-console-todo-app/ and the speckit.specify file in the root directory as required.