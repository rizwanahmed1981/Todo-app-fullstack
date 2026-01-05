# Task List: Console Todo App - Phase I

**Feature**: Console Todo App
**Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md) | **Date**: 2026-01-05

## Overview
This task list implements the Console Todo App with in-memory storage supporting all five core features (Add, List, Update, Delete, Complete). The implementation follows Python 3.14 standards with UV package management, using dataclasses for models and modular design principles.

## Implementation Strategy
- **MVP Scope**: User Story 1 (Add and View Tasks) for initial working application
- **Incremental Delivery**: Each user story builds on the previous, maintaining a working application
- **Parallel Execution**: Tasks marked [P] can run simultaneously if they modify different files
- **TDD Approach**: Test tasks are included and should be completed before implementation

## Dependencies
- **User Story 2** depends on User Story 1 completion
- **User Story 3** depends on User Story 1 completion
- **Foundational Phase** must complete before any user story phases

---

## Phase 1: Setup

- [ ] T001 Create project directory structure for phase1/
- [ ] T002 Create pyproject.toml with Python 3.14 requirement and UV configuration
- [ ] T003 Create initial README.md with setup instructions
- [ ] T004 Create CLAUDE.md with project-specific instructions
- [ ] T005 Create phase1/src/ directory structure
- [ ] T006 Create phase1/tests/ directory structure

## Phase 2: Foundational Components

- [ ] T010 [P] Create models.py with Task dataclass and custom exceptions
- [ ] T011 [P] Create constants.py with app constants and messages
- [ ] T012 [P] Create display.py with formatting and output utilities
- [ ] T013 Create task_manager.py with in-memory storage and business logic
- [ ] T014 Create main.py with entry point and command loop
- [ ] T015 [P] Create tests/test_models.py with Task model tests
- [ ] T016 [P] Create tests/test_task_manager.py with business logic tests

## Phase 3: [US1] Add and View Tasks (Priority: P1)

- [ ] T020 [P] [US1] Implement Task model with validation in models.py
- [ ] T021 [P] [US1] Implement TaskNotFoundError and ValidationError exceptions in models.py
- [ ] T022 [P] [US1] Implement Task creation with auto-increment ID in models.py
- [ ] T023 [P] [US1] Implement Task display formatting in display.py
- [ ] T024 [US1] Implement TaskManager.add_task() method in task_manager.py
- [ ] T025 [US1] Implement TaskManager.list_tasks() method in task_manager.py
- [ ] T026 [US1] Implement 'add' command in main.py
- [ ] T027 [US1] Implement 'list' command in main.py
- [ ] T028 [US1] Implement welcome message and menu in main.py
- [ ] T029 [P] [US1] Create tests for add functionality in tests/test_task_manager.py
- [ ] T030 [P] [US1] Create tests for list functionality in tests/test_task_manager.py

## Phase 4: [US2] Update and Complete Tasks (Priority: P2)

- [ ] T035 [P] [US2] Implement Task.update() method in models.py
- [ ] T036 [P] [US2] Implement Task.mark_complete() method in models.py
- [ ] T037 [US2] Implement TaskManager.update_task() method in task_manager.py
- [ ] T038 [US2] Implement TaskManager.complete_task() method in task_manager.py
- [ ] T039 [US2] Implement TaskManager.delete_task() method in task_manager.py
- [ ] T040 [US2] Implement 'update' command in main.py
- [ ] T041 [US2] Implement 'complete' command in main.py
- [ ] T042 [US2] Implement 'delete' command in main.py
- [ ] T043 [P] [US2] Create tests for update functionality in tests/test_task_manager.py
- [ ] T044 [P] [US2] Create tests for complete functionality in tests/test_task_manager.py
- [ ] T045 [P] [US2] Create tests for delete functionality in tests/test_task_manager.py

## Phase 5: [US3] Error Handling (Priority: P3)

- [ ] T050 [P] [US3] Implement input validation in task_manager.py
- [ ] T051 [P] [US3] Implement error handling for invalid commands in main.py
- [ ] T052 [P] [US3] Implement error handling for invalid task IDs in task_manager.py
- [ ] T053 [US3] Implement 'help' command in main.py
- [ ] T054 [US3] Implement 'exit' command in main.py
- [ ] T055 [P] [US3] Create tests for error handling in tests/test_task_manager.py
- [ ] T056 [P] [US3] Create tests for invalid commands in tests/test_main.py
- [ ] T057 [P] [US3] Create tests for edge cases in tests/test_validation.py

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T060 Add type hints to all functions in all modules
- [ ] T061 Add docstrings to all functions and classes
- [ ] T062 Run pytest tests/ to verify all tests pass
- [ ] T063 Run type checking with mypy
- [ ] T064 Format code with black
- [ ] T065 Run linting with ruff
- [ ] T066 Update README.md with usage instructions
- [ ] T067 Create .gitignore with appropriate patterns
- [ ] T068 Create .pre-commit-config.yaml for automated checks

---

## Parallel Execution Examples

**Phase 3 [US1] - Can run in parallel:**
- Tasks T020-T023: Model and display components
- Tasks T029-T030: Test creation

**Phase 4 [US2] - Can run in parallel:**
- Tasks T035-T036: Model methods
- Tasks T043-T045: Test creation

**Phase 5 [US3] - Can run in parallel:**
- Tasks T050-T052: Error handling implementation
- Tasks T055-T057: Test creation

## User Story Completion Order

1. **Complete User Story 1** → Add and View Tasks (P1)
2. **Complete User Story 2** → Update and Complete Tasks (P2)
3. **Complete User Story 3** → Error Handling (P3)

Each user story provides an independently testable increment with complete functionality.