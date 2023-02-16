from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
import datetime

from sqlalchemy.orm import relationship

from app.database.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    active = Column(Boolean)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime)
    teacherId = Column(Integer, ForeignKey("users.id"))
    studentCourses = relationship("StudentCourse", back_populates="course")
    courseLikes = relationship("CourseLike", back_populates="course")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
