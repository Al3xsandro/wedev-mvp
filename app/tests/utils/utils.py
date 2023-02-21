import random
import string

from sqlalchemy.orm import Session

from app.core.settings import DEFAULT_USER, DEFAULT_PASSWORD

import app.crud.user as crud
from app.schemas.user import UserCreate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=14))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def create_staff_user(db: Session):
    user_obj = UserCreate(
        firstName="John",
        lastName="Leao",
        email=DEFAULT_USER,
        password=DEFAULT_PASSWORD,
        role="STUDENT",
        state="SP",
        city="SP",
        address="Rua José Pereira Fontes",
        postalCode="00000-000",
    )

    crud.create(db, user_obj=user_obj)
