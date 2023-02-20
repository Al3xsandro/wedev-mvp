from sqlalchemy.orm import Session
from app.core.security import getPasswordHash

import app.crud.user as crud
from app.database.models import User, PhoneNumber
from app.core.settings import DEFAULT_USER, DEFAULT_PASSWORD


def init_db(db: Session):
    user = crud.getUserByEmail(db, DEFAULT_USER)

    if not user:
        user_obj = User(
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

        phones = PhoneNumber(user=user_obj, phoneNumber="5554-1535")

        user_obj.phoneNumbers = [phones]

        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
