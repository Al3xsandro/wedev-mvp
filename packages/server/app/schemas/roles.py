from pydantic import BaseModel
from enum import Enum


class RoleEnum(str, Enum):
    teacher = "TEACHER"
    student = "STUDENT"
    staff = "STAFF"


class Roles(BaseModel):
    roles: RoleEnum
