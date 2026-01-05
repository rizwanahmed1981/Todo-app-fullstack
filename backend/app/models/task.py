from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime


class TaskBase(SQLModel):
    """
    Base model for Task with shared attributes.
    """
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str = Field(foreign_key="user.id")


class Task(TaskBase, table=True):
    """
    Task model representing a todo item in the system.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

    # Relationship to User (managed by Better Auth)
    # user: User = Relationship(back_populates="tasks")