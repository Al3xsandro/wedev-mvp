from fastapi import APIRouter, Body, Depends, HTTPException

from app.database.database import get_db
from sqlalchemy.orm import Session
import app.crud.course as crud

from app.database.models import User
from app.schemas.course import CourseCreate, CourseResponse

from app.api.middlewares import getCurrentUser, isStaff

router = APIRouter()


@router.get(
    "/courses/:id",
    name="Acessar curso",
    description="Acessar curso cadastrado",
    response_model=CourseResponse,
)
def get_course(
    id: int, db: Session = Depends(get_db), user: User = Depends(getCurrentUser)
):
    return {"id": 1}


@router.post(
    "/courses",
    name="Criar curso",
    description="Essa rota permite que você crie um curso na plataforma",
    response_model=CourseResponse,
)
def create_course(
    db: Session = Depends(get_db),
    user: User = Depends(isStaff),
    course_obj: CourseCreate = Body(),
):
    course = crud.create(db, course_obj=course_obj)
    return course


# get all course students by id

# delete course

# get all courses and add pagination
