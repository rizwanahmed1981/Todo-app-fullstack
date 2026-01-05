# 001: Prompt to Generate Development Tasks

Generate a concise list of development tasks for the `001-console-todo-app` project.

You must adhere strictly to the project's constitution, specification, and plan. The output should be a list of short, imperative tasks.

**Prompt for `claude cli`:**

```
Generate a sequence of development tasks to implement the console-based todo application.

**Instructions:**
1.  **Source of Truth:** Base all tasks on `specs/001-console-todo-app/spec.md` and `specs/001-console-todo-app/plan.md`.
2.  **Constitutional Compliance:** Ensure every task implicitly follows the rules in `.specify/memory/constitution.md`, especially concerning Python 3.14, `uv`, type hints, and testing.
3.  **Output Format:** Provide a numbered list of short, imperative commands for a developer.

**Task Breakdown:**
- Start with project setup and directory structure as per the plan.
- Create tasks for each component: `models.py`, `task_manager.py`, `display.py`, `main.py`.
- For each piece of business logic (e.g., adding a task), generate a corresponding task to write a unit test.
- Include tasks for ensuring code quality (e.g., adding docstrings and type hints).
```
