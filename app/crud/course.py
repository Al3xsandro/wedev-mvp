from fastapi import HTTPException
from sqlalchemy import func

from sqlalchemy.orm import Session
from app.database.models import Course, User
from app.schemas.course import CourseCreate


def create(db: Session, course_obj: CourseCreate):
    db_course = Course(
        name=course_obj.name,
        active=course_obj.is_active,
        start_date=course_obj.start_date,
        end_date=course_obj.end_date,
        teacherId=course_obj.teacherId,
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


def getCourses(
    db: Session, isActive: bool, name: str = None, skip: int = 0, limit: int = 100
):
    courses = db.query(Course).filter(Course.active == isActive)

    if name is not None:
        return courses.filter(Course.name.ilike(f"%{name}%")).all()

    return courses.offset(skip).limit(limit).all()


def getCoursesByTeacher(
    db: Session,
    teacher_id: int,
    isActive: bool,
    name: str = None,
    skip: int = 0,
    limit: int = 100,
):
    courses = (
        db.query(Course)
        .filter(Course.teacherId == teacher_id)
        .filter(Course.active == isActive)
    )

    if name is not None:
        return courses.filter(Course.name.ilike(f"%{name}%")).all()

    return courses.offset(skip).limit(limit).all()


def getCourseById(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()

    # todo: add this reposibility to database
    # query = (
    #   db.query(Course, func.count(User.id).label("totalStudents"))
    #     .outerjoin(Course.students)
    #     .group_by(Course.id)
    # )

    return {
        "course": course,
        "totalStudents": len(course.students),
        "totalLikes": len(course.courseLikes),
    }


def addStudentToCourse(db: Session, student_id: int, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    student = db.query(User).filter(User.id == student_id).first()

    if not course:
        raise HTTPException(
            status_code=400,
            detail="ID inválido, verifique se esse curso está cadastrado na plataforma",
        )

    if not student or student.role != "STUDENT":
        raise HTTPException(
            status_code=400,
            detail="ID inválido, verifique se este aluno está cadastrado na plataforma",
        )

    course.students.append(student)

    db.add(course)
    db.commit()
    return "Aluno adicionado com sucesso!"


def likeCourse(db: Session, userId: int, courseId: int):
    course = db.query(Course).filter(Course.id == courseId).first()
    user = db.query(User).filter(User.id == userId).first()

    if not course:
        raise HTTPException(
            status_code=400,
            detail="ID inválido, verifique se esse curso está cadastrado na plataforma",
        )

    course.courseLikes.append(user)
    db.commit()
    return "Avalição adicionada com sucesso!"
