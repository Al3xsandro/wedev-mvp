from fastapi import APIRouter, Query, Body, Depends

from app.database.database import get_db
from sqlalchemy.orm import Session

from app.schemas.user import UserSchema, UserResponse
from app.schemas.token import TokenSchema

from app.database.models import User
from app.api.middlewares import getCurrentUser, isStaff

router = APIRouter()


@router.get(
    "/me",
    name="Dados do usuário",
    description="Essa rota deve retornar as informações do usuário junto com o tipo de conta dentro da plataforma",
    response_model=UserSchema,
)
def getUser(db: Session = Depends(get_db), user: User = Depends(getCurrentUser)):
    return


@router.post(
    "/",
    name="Criar usuário",
    description="Essa rota permite que staffs criem novas contas do tipo aluno e professor na plataforma",
    status_code=201,
    response_model=TokenSchema,
)
def createUser(db: Session = Depends(get_db), user: UserSchema = Body()):
    return


@router.put(
    "/{user_id}",
    name="Atualizar usuário",
    description="Essa rota permite atualizar as inforamções do usuário",
    status_code=200,
    response_model=UserResponse,
)
def updateUse(
    db: Session = Depends(get_db),
    user_id: str = Query(),
    user: User = Depends(getCurrentUser),
):
    return


@router.delete(
    "/{user_id}",
    name="Deletar usuário",
    description="Essa rota permite que staffs deletem contas do tipo aluno e professor na plataforma",
    status_code=200,
    response_model=None,
)
def deleteUser(
    db: Session = Depends(get_db), user_id: str = Query(), user: User = Depends(isStaff)
):
    return
