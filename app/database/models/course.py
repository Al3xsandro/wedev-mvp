from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
import datetime

from sqlalchemy.orm import relationship

from app.database.database import Base


from typing import TYPE_CHECKING, List

from .studentCourse import StudentCourse
from .courseLike import CourseLike

if TYPE_CHECKING:
    from courseLike import CourseLike
    from user import User


class Course(Base):
    __tablename__ = "courses"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    active = Column(Boolean)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime)
    teacherId = Column(Integer, ForeignKey("users.id"))
    students: List["User"] = relationship(
        "User", secondary=StudentCourse, back_populates="studentCourses"
    )
    courseLikes: List["CourseLike"] = relationship(
        "User", secondary=CourseLike, back_populates="studentLikes"
    )
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
