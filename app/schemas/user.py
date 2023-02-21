import re
from pydantic import BaseModel, EmailStr, validator
from app.schemas.role import RoleEnum

from typing import Optional, List
from datetime import date

from pydantic import BaseModel

from app.schemas.phoneNumber import PhoneNumberResponse


class UserSchema(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    role: RoleEnum
    state: str
    city: str
    address: str
    postalCode: str

    class Config:
        orm_mode = True


class UserCreate(UserSchema):
    phoneNumbers: List[str] = ["0000-0000"]
    password: str

    @validator("phoneNumbers", each_item=True)
    def phone_validation(cls, v):
        regex = r"^\d{4}-\d{4}$"
        if v and not re.search(regex, v, re.I):
            raise ValueError("Phone Number Invalid.")
        return v


class UserResponse(UserSchema):
    id: Optional[int] = None
    phoneNumbers: List[PhoneNumberResponse]
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
