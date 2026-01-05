from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from app.models import Task, TaskBase
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.database.database import get_session
from datetime import datetime


router = APIRouter()


@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    user_id: str,
    session: Session = Depends(get_session),
    completed: bool = None,
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve a list of tasks for a specific user.

    Args:
        user_id: ID of the user whose tasks to retrieve
        session: Database session
        completed: Optional filter for completed status
        skip: Number of records to skip
        limit: Maximum number of records to return

    Returns:
        List of TaskResponse objects
    """
    # Build the query with user_id filter
    query = select(Task).where(Task.user_id == user_id)

    # Apply completed filter if specified
    if completed is not None:
        query = query.where(Task.completed == completed)

    # Apply pagination
    query = query.offset(skip).limit(limit)

    tasks = session.exec(query).all()
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific task by ID for a specific user.

    Args:
        user_id: ID of the user who owns the task
        task_id: ID of the task to retrieve
        session: Database session

    Returns:
        TaskResponse object

    Raises:
        HTTPException: If task not found or doesn't belong to user
    """
    task = session.get(Task, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this task"
        )

    return task


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,
    task_create: TaskCreate,
    session: Session = Depends(get_session)
):
    """
    Create a new task for a specific user.

    Args:
        user_id: ID of the user creating the task
        task_create: Task creation data
        session: Database session

    Returns:
        TaskResponse object

    Raises:
        HTTPException: If validation fails
    """
    # Validate title length
    if not (1 <= len(task_create.title) <= 200):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title must be between 1 and 200 characters"
        )

    if task_create.description and len(task_create.description) > 1000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Description must not exceed 1000 characters"
        )

    # Create the task
    task = Task(
        title=task_create.title,
        description=task_create.description,
        user_id=user_id,
        completed=False  # Default to not completed
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    user_id: str,
    task_id: int,
    task_update: TaskUpdate,
    session: Session = Depends(get_session)
):
    """
    Update an existing task for a specific user.

    Args:
        user_id: ID of the user who owns the task
        task_id: ID of the task to update
        task_update: Task update data
        session: Database session

    Returns:
        TaskResponse object

    Raises:
        HTTPException: If task not found, doesn't belong to user, or validation fails
    """
    task = session.get(Task, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )

    # Validate title if provided
    if task_update.title is not None:
        if not (1 <= len(task_update.title) <= 200):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title must be between 1 and 200 characters"
            )
        task.title = task_update.title

    # Validate description if provided
    if task_update.description is not None:
        if len(task_update.description) > 1000:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Description must not exceed 1000 characters"
            )
        task.description = task_update.description

    # Update completion status if provided
    if task_update.completed is not None:
        task.completed = task_update.completed
        task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session)
):
    """
    Delete a specific task for a specific user.

    Args:
        user_id: ID of the user who owns the task
        task_id: ID of the task to delete
        session: Database session

    Raises:
        HTTPException: If task not found or doesn't belong to user
    """
    task = session.get(Task, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task"
        )

    session.delete(task)
    session.commit()


@router.patch("/{task_id}/complete", response_model=TaskResponse)
def toggle_task_completion(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a specific task for a specific user.

    Args:
        user_id: ID of the user who owns the task
        task_id: ID of the task to update
        session: Database session

    Returns:
        TaskResponse object with updated completion status
    """
    task = session.get(Task, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )

    # Toggle completion status
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)

    return task