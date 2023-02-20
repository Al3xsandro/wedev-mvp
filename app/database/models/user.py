from sqlalchemy import Column, Enum, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

from app.schemas.roles import RoleEnum

from app.database.database import Base

from typing import TYPE_CHECKING, List

from .studentCourse import StudentCourse
from .courseLike import CourseLike

if TYPE_CHECKING:
    from phoneNumber import PhoneNumber
    from courseLike import CourseLike


class User(Base):
    __tablename__ = "users"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.student)
    state = Column(String)
    city = Column(String)
    address = Column(String)
    postalCode = Column(String)
    phoneNumbers: List["PhoneNumber"] = relationship(
        "PhoneNumber", back_populates="user"
    )
    studentCourses: List["StudentCourse"] = relationship(
        "Course", secondary=StudentCourse, back_populates="students"
    )
    studentLikes: List["CourseLike"] = relationship(
        "Course", secondary=CourseLike, back_populates="courseLikes"
    )
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
