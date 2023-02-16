from sqlalchemy.orm import Session

import app.crud.user as crud
from app.schemas.user import UserCreate

from app.tests.utils import utils


def test_create_student_user(db: Session):
    email = utils.random_email()
    password = utils.random_lower_string()

    user_obj = UserCreate(
        firstName="John",
        lastName="Leao",
        email=email,
        password=password,
        role="STUDENT",
        state="SP",
        city="SP",
        address="Rua José Pereira Fontes",
        postalCode="00000-000",
    )

    user = crud.create(db, user_obj=user_obj)
    assert user.email == email
