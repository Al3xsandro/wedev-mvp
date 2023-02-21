from typing import Generator

from fastapi import Depends, HTTPException, status

from app.database.database import get_db
from sqlalchemy.orm import Session

from app.core.settings import ALGORITHM, SECRET_KEY
import app.crud.user as crud
from app.schemas.token import TokenPayload
from app.database.models import User

from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError

from jose import jwt

from app.database.database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/session/auth")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def getCurrentUser(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Suas credenciais estão inválidas",
        )

    user = crud.getUserById(db, token_data.sub)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user


def isStaff(
    currentUser: User = Depends(getCurrentUser),
):
    if not crud.isStaff(currentUser.role):
        raise HTTPException(
            status_code=401, detail="Você não tem permissão para executar esta ação"
        )
    return currentUser
