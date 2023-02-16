from sqlalchemy.orm import Session
from app.core.security import getPasswordHash

import app.crud.user as crud
from app.schemas.user import UserCreate
from app.core.settings import DEFAULT_USER, DEFAULT_PASSWORD


def init_db(db: Session):
    user = crud.getUserByEmail(db, DEFAULT_USER)

    if not user:
        user_obj = UserCreate(
            firstName="John",
            lastName="Leao",
            email=DEFAULT_USER,
            password=getPasswordHash(DEFAULT_PASSWORD),
            role="STAFF",
            state="SP",
            city="SP",
            address="Rua José Pereira Fontes",
            postalCode="00000-000",
        )

        crud.UserCreate(db, user_obj)
