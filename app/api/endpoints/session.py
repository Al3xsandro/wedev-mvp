from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.database.database import get_db
from sqlalchemy.orm import Session

import app.crud.user as crud
from app.schemas.token import TokenSchema
from app.schemas.user import UserSchema

from app.core.jwt import createAccessToken
from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES

from datetime import timedelta

router = APIRouter()


@router.post(
    "/auth",
    name="Obter token",
    description="Essa rota deve retornar o token jwt para autenticação",
    response_model=TokenSchema,
)
def auth(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user: UserSchema = crud.authenticate(
        db, email=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    token = createAccessToken(
        data={"role": user.role},
        subject=user.id,
        expires_delta=timedelta(ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }
