from pydantic import BaseModel, EmailStr
from app.schemas.roles import RoleEnum

from typing import Optional, List
from datetime import date

from pydantic import BaseModel

from app.schemas.phoneNumber import PhoneNumber


class UserSchema(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    role: RoleEnum
    state: str
    city: str
    address: str
    postalCode: str


class UserCreate(UserSchema):
    password: str


class UserResponse(UserSchema):
    id: Optional[int] = None
    phoneNumbers: List[PhoneNumber]
    created_at: Optional[date] = None

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    postalCode: Optional[str] = None
