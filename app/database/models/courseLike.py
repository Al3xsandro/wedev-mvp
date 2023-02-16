from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database.database import Base


class CourseLike(Base):
    __tablename__ = "courseLikes"

    id = Column(Integer, primary_key=True, index=True)
    courseId = Column(Integer, ForeignKey("courses.id"))
    studentId = Column(Integer, ForeignKey("users.id"))

    student = relationship("User", back_populates="studentLikes")
    course = relationship("Course", back_populates="courseLikes")
