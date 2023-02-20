from sqlalchemy import Column, ForeignKey, Integer, Table

from app.database.database import Base

CourseLike = Table(
    "courseLikes",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("courseId", Integer, ForeignKey("courses.id")),
    Column("studentId", Integer, ForeignKey("users.id")),
)
