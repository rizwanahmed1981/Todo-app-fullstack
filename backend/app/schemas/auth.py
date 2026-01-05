from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    """
    Base schema for User with shared attributes.
    """
    email: str
    name: Optional[str] = None


class UserCreate(UserBase):
    """
    Schema for creating a new User.
    """
    email: str
    name: Optional[str] = None
    password: str


class UserLogin(BaseModel):
    """
    Schema for user login.
    """
    email: str
    password: str


class UserResponse(UserBase):
    """
    Schema for User response with additional fields.
    """
    id: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    """
    Token response model.
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Token data model.
    """
    user_id: Optional[str] = None