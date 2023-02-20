from fastapi import APIRouter, Body, Depends, Query, HTTPException
from typing import Optional, List

from app.database.database import get_db
from sqlalchemy.orm import Session
import app.crud.course as crud

from app.database.models import User
from app.schemas.course import (
    CourseCreate,
    CourseResponse,
    CourseResponseTeacher,
    CourseResponseCount,
)

from app.api.middlewares import getCurrentUser, isStaff

router = APIRouter()


@router.get(
    "/all",
    name="Listar todos os cursos da plataforma",
    description="Listar todos os cursos cadastrados na plataforma",
    tags=["Staff"],
    response_model=List[CourseResponseTeacher],
)
def get_courses(
    db: Session = Depends(get_db),
    isActive: Optional[bool] = Query(default=True, alias="IsActive"),
    name: Optional[str] = Query(default=None, alias="Name"),
    skip: Optional[int] = Query(default=None, alias="Skip"),
    limit: Optional[int] = Query(default=None, alias="Limit"),
    user: User = Depends(isStaff),
):
    courses = crud.getCourses(db, isActive, name, skip, limit)
    return courses


@router.get(
    "/teacher/all",
    name="Listar cursos do professor",
    description="Listar todos os cursos relacionados ao seu user-id",
    tags=["Professor"],
    response_model=List[CourseResponseTeacher],
)
def get_teacher_courses(
    db: Session = Depends(get_db),
    isActive: Optional[bool] = Query(default=True, alias="IsActive"),
    name: Optional[str] = Query(default=None, alias="Name"),
    skip: Optional[int] = Query(default=None, alias="Skip"),
    limit: Optional[int] = Query(default=None, alias="Limit"),
    user: User = Depends(getCurrentUser),
):
    if user.role != "TEACHER":
        raise HTTPException(status_code=400, detail="Você não é um professor")

    courses = crud.getCoursesByTeacher(db, user.id, isActive, name, skip, limit)
    return courses


@router.get(
    "/student/all",
    name="Listar cursos do aluno",
    description="Listar todos os cursos relacionados ao seu user-id",
    response_model=List[CourseResponse],
    tags=["Aluno"],
)
def get_student_courses(
    db: Session = Depends(get_db), user: User = Depends(getCurrentUser)
):
    if user.role != "STUDENT":
        raise HTTPException(status_code=400, detail="Você não é um aluno")

    return user.studentCourses


@router.get(
    "/{course_id}",
    name="Acessar curso",
    description="Acessar curso cadastrado",
    tags=["Staff"],
    response_model=CourseResponseCount,
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(isStaff),
):
    course = crud.getCourseById(db, course_id)

    if not course:
        raise HTTPException(
            status_code=400, detail="Não há cursos cadastrados com esse id"
        )

    return course


@router.post(
    "/",
    name="Criar curso",
    description="Essa rota permite que você crie um curso na plataforma",
    response_model=CourseResponse,
    status_code=201,
    tags=["Staff"],
)
def create_course(
    db: Session = Depends(get_db),
    user: User = Depends(isStaff),
    course_obj: CourseCreate = Body(),
):
    course = crud.create(db, course_obj=course_obj)
    return course


@router.post(
    "/student",
    name="Adicionar estudante a um curso",
    description="Essa rota permite que você adicione um aluno em um curso",
    tags=["Staff"],
)
def add_student(
    db: Session = Depends(get_db),
    student_id: int = Body(),
    course_id: int = Body(),
    user: User = Depends(isStaff),
):
    user = crud.addStudentToCourse(db=db, student_id=student_id, course_id=course_id)
    return user


@router.post(
    "/{course_id}/like/",
    name="Avaliar curso",
    description="Essa rota permite que você avalie um curso que esteja matriculado",
    tags=["Usuários"],
)
def like_course(
    db: Session = Depends(get_db),
    course_id: int = Query(),
    user: User = Depends(getCurrentUser),
):
    return crud.likeCourse(db, userId=user.id, courseId=course_id)
