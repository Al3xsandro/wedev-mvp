from pydantic import BaseModel

from typing import Optional
from datetime import date


class CourseSchema(BaseModel):
    name: str
    is_active: Optional[bool] = True
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    teacherId: str


class CourseCreate(CourseSchema):
    pass


class CourseResponse(CourseSchema):
    id: Optional[int] = None
    created_at: Optional[date] = None

    class Config:
        orm_mode = True
