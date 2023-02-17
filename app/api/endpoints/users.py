from fastapi import APIRouter, Query, Body, Depends, HTTPException

from app.database.database import get_db
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserUpdate

from fastapi.templating import Jinja2Templates

import app.crud.user as crud

from app.database.models import User
from app.api.middlewares import getCurrentUser, isStaff


router = APIRouter()


@router.get(
    "/me",
    name="Dados do usuário",
    description="Essa rota deve retornar as informações do usuário junto com o tipo de conta dentro da plataforma",
    response_model=UserResponse,
    tags=["Usuários"],
)
def get_user(db: Session = Depends(get_db), user: User = Depends(getCurrentUser)):
    return user


@router.post(
    "/",
    name="Criar usuário",
    description="Essa rota permite que staffs criem novas contas do tipo aluno e professor na plataforma",
    status_code=201,
    response_model=UserResponse,
    tags=["staff"],
)
def create_user(
    db: Session = Depends(get_db),
    user: User = Depends(isStaff),
    user_obj: UserCreate = Body(),
):
    user = crud.getUserByEmail(db, user_obj.email)

    if user:
        raise HTTPException(
            status_code=400, detail="Esse endereço de e-mail já está em uso"
        )

    user = crud.create(db, user_obj=user_obj)

    return user


@router.put(
    "/",
    name="Atualizar usuário",
    description="Essa rota permite atualizar as inforamções do usuário",
    status_code=200,
    response_model=UserUpdate,
    tags=["Usuários"],
)
def update_user(
    db: Session = Depends(get_db),
    user: User = Depends(getCurrentUser),
    user_obj: UserUpdate = Body(),
):
    new_user = user_obj.dict(exclude_unset=True)
    user_updated = crud.update(db, user_id=user.id, user_obj=new_user)

    if user_updated != 1:
        raise HTTPException(
            status_code=400,
            detail="Ocorreu um erro durante a execução do update, tente novamente",
        )

    return new_user


@router.delete(
    "/{user_id}",
    name="Deletar usuário",
    description="Essa rota permite que staffs deletem contas do tipo aluno e professor na plataforma",
    status_code=200,
    response_model=None,
    tags=["Staff"],
)
def delete_user(
    db: Session = Depends(get_db), user_id: int = Query(), user: User = Depends(isStaff)
):
    return crud.deleteUser(db, user_id)
