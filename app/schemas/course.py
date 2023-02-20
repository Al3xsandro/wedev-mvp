from pydantic import BaseModel

from typing import Optional, List
from datetime import date

from app.schemas.user import UserSchema


class CourseSchema(BaseModel):
    name: str
    is_active: Optional[bool] = True
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    teacherId: int


class CourseCreate(CourseSchema):
    pass


class CourseResponse(CourseSchema):
    id: Optional[int] = None
    created_at: Optional[date] = None

    class Config:
        orm_mode = True


class CourseResponseTeacher(CourseSchema):
    id: Optional[int] = None
    students: List[UserSchema]
    created_at: Optional[date] = None

    class Config:
        orm_mode = True
