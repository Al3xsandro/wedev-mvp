from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class StudentCourse(Base):
    __tablename__ = "studentCourses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    courseId = Column(Integer, ForeignKey("courses.id"))
    studentId = Column(Integer, ForeignKey("users.id"))

    student = relationship("User", back_populates="studentCourses")
    course = relationship("Course", back_populates="studentCourses")
