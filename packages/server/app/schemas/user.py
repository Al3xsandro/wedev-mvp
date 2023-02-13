from pydantic import BaseModel
from app.schemas.roles import RoleEnum

from typing import Optional
from datetime import date

from pydantic import BaseModel


class UserSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    role: RoleEnum
    state: str
    city: str
    address: str
    postalCode: str
    created_at: Optional[date] = None


class UserCreate(UserSchema):
    pass


class UserUpdate(UserSchema):
    password: Optional[str] = None


class UserResponse(BaseModel):
    firstName: str
    lastName: str
    email: str
    role: RoleEnum
    state: str
    city: str
    address: str
    postalCode: str
