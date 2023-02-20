from sqlalchemy import Column, ForeignKey, Integer, Table

from app.database.database import Base

StudentCourse = Table(
    "studentCourses",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("userId", Integer, ForeignKey("courses.id")),
    Column("courseId", Integer, ForeignKey("users.id")),
)
