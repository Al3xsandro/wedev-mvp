from pydantic import BaseModel
from enum import Enum


class RoleEnum(str, Enum):
    teacher = "TEACHER"
    student = "STUDENT"
    staff = "STAFF"


class Role(BaseModel):
    role: RoleEnum
