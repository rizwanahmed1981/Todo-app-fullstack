from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    """
    Base schema for Task with shared attributes.
    """
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    """
    Schema for creating a new Task.
    """
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    """
    Schema for updating an existing Task.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(TaskBase):
    """
    Schema for Task response with additional fields.
    """
    id: int
    user_id: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True