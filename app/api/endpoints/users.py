from fastapi import APIRouter, Query, Body, Depends, HTTPException

from typing import Optional, List

from app.database.database import get_db
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserUpdate

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


@router.get(
    "/all",
    name="Usuários cadastrados",
    description="Essa rota deve retornar as informações de todos os usuário junto com o tipo de conta dentro da plataforma",
    response_model=List[UserResponse],
    tags=["Staff"],
)
def get_user(
    db: Session = Depends(get_db),
    skip: Optional[int] = Query(default=None, alias="Skip"),
    limit: Optional[int] = Query(default=None, alias="Limit"),
    user: User = Depends(isStaff),
):
    users = crud.getAllUsers(db, skip, limit)
    return users


@router.post(
    "/",
    name="Criar usuário",
    description="Essa rota permite que staffs criem novas contas do tipo aluno e professor na plataforma",
    status_code=201,
    response_model=UserResponse,
    tags=["Staff"],
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
    description="Essa rota permite atualizar as informações do usuário",
    status_code=200,
    response_model=UserUpdate,
    tags=["Usuários"],
)
def update_user(
    db: Session = Depends(get_db),
    user: User = Depends(getCurrentUser),
    user_obj: UserUpdate = Body(),
):
    new_user = user_obj.dict(exclude_none=True)
    user_updated = crud.update(db, user=user, user_obj=new_user)

    if user_updated != 1:
        raise HTTPException(
            status_code=400,
            detail="Ocorreu um erro durante a execução do update, tente novamente",
        )

    return new_user
