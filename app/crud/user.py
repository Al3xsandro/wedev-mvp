from sqlalchemy.orm import Session
from app.database.models import User
from app.schemas.user import UserSchema, UserCreate

from app.core.security import getPasswordHash, verifyPassword


def create(db: Session, user_obj: UserCreate):
    db_user = User(
        firstName=user_obj.firstName,
        lastName=user_obj.lastName,
        email=user_obj.email,
        password=getPasswordHash(user_obj.password),
        role=user_obj.role,
        state=user_obj.state,
        city=user_obj.city,
        address=user_obj.address,
        postalCode=user_obj.postalCode,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def getUserById(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def update(db: Session, user_id: int, user_obj: User):
    user = db.query(User).filter(User.id == user_id).update(user_obj)
    db.commit()
    return user


def getUserByEmail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def authenticate(db: Session, email: str, password: str):
    user: UserSchema = getUserByEmail(db, email)

    if not user:
        return False
    if not verifyPassword(password, user.password):
        return False

    return user


def deleteUser(db: Session, id: int):
    db.query(User).filter(User.id == id).delete(synchronize_session="auto")
    db.commit()
    return


def isStaff(role: str):
    return role == "STAFF"
