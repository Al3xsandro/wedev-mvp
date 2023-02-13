from sqlalchemy import Column, Enum, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

from app.schemas.roles import RoleEnum

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

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
    phoneNumbers = relationship("PhoneNumber", back_populates="user")
    studentCourses = relationship("StudentCourse", back_populates="student")
    studentLikes = relationship("CourseLike", back_populates="student")
    created_at =  Column(DateTime, default=datetime.datetime.utcnow)
