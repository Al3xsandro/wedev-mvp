from sqlalchemy.orm import Session
from app.database.models import Course
from app.schemas.course import CourseCreate


def create(db: Session, course_obj: CourseCreate):
    db_course = Course(
        name=course_obj.name,
        is_active=course_obj.is_active,
        start_date=course_obj.start_date,
        end_date=course_obj.end_date,
        teacherId=course_obj.teacherId,
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course
