from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm

from app.database.database import get_db
from sqlalchemy.orm import Session

from fastapi.templating import Jinja2Templates

import app.crud.user as crud
from app.schemas.user import UserSchema

from app.core.jwt import createAccessToken
from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES

from datetime import timedelta

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/login", include_in_schema=False)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post(
    "/auth",
    name="Obter token",
    description="Essa rota deve retornar o token jwt para autenticação",
    include_in_schema=False,
)
def auth(
    request: Request,
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    errors = []
    user: UserSchema = crud.authenticate(
        db, email=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    response = templates.TemplateResponse(
        "login.html", {"request": request, "erros": errors}
    )

    access_token = createAccessToken(
        data=dict({"role": user.role}),
        subject=user.id,
        expires_delta=timedelta(ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )

    return response
