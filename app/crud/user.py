from sqlalchemy.orm import Session
from app.database.models import User, PhoneNumber
from app.schemas.user import UserSchema, UserCreate

from app.core.security import getPasswordHash, verifyPassword


def getAll(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


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

    phones = []

    for number in user_obj.phoneNumbers:
        phone = PhoneNumber(user=db_user, phoneNumber=number)
        phones.append(phone)

    db_user.phoneNumbers = phones

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def getUserById(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def update(db: Session, user: User, user_obj: User):
    user = db.query(User).filter(User.id == user.id).update(user_obj)
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


def isStaff(role: str):
    return role == "STAFF"


def getAllUsers(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(User).join(PhoneNumber.user).offset(skip).limit(limit).all()
    return users
