from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserProfileBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Full name of the user")
    email: Optional[str] = Field(None, description="Email address of the user")
    bio: Optional[str] = Field(None, max_length=500, description="Short user biography")

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[str] = Field(None)
    bio: Optional[str] = Field(None, max_length=500)

class UserProfile(UserProfileBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Title of the todo item")
    description: Optional[str] = Field(None, max_length=1000, description="Detailed description of the todo item")
    completed: bool = Field(False, description="Completion status of the todo item")
    priority: str = Field("medium", description="Priority level: low, medium, high")
    category: Optional[str] = Field("General", description="Category or tag for the todo item")

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None
    priority: Optional[str] = None
    category: Optional[str] = None

class TodoItem(TodoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
