from pydantic import BaseModel

from typing import Optional
from datetime import date


class CourseSchema(BaseModel):
    name: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    teacherId: str
