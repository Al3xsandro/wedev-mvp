from fastapi import APIRouter, Body, Depends, HTTPException

from app.database.database import get_db
from sqlalchemy.orm import Session
import app.crud.course as crud

from app.database.models import User
from app.schemas.course import CourseCreate, CourseResponse

from app.api.middlewares import getCurrentUser, isStaff

router = APIRouter()


@router.get(
    "/all",
    name="Listar todos os cursos da plataforma",
    description="Listar todos os cursos cadastrados na plataforma",
    response_model=CourseResponse,
    tags=["Staff"],
)
def get_courses(
    db: Session = Depends(get_db),
    user: User = Depends(isStaff),
):
    courses = crud.getCourses(db)
    return courses


@router.get(
    "/all/me",
    name="Listar meus cursos",
    description="Listar todos os cursos relacionados ao seu user-id",
    response_model=CourseResponse,
    tags=["Cursos"],
)
def get_my_courses():
    return


@router.get(
    "/:id",
    name="Acessar curso",
    description="Acessar curso cadastrado",
    response_model=CourseResponse,
    tags=["Cursos"],
)
def get_course(
    id: int, db: Session = Depends(get_db), user: User = Depends(getCurrentUser)
):
    return {"id": 1}


@router.post(
    "/",
    name="Criar curso",
    description="Essa rota permite que você crie um curso na plataforma",
    response_model=CourseResponse,
    tags=["Cursos"],
)
def create_course(
    db: Session = Depends(get_db),
    user: User = Depends(isStaff),
    course_obj: CourseCreate = Body(),
):
    course = crud.create(db, course_obj=course_obj)
    return course


# delete course

# get all courses and add pagination
