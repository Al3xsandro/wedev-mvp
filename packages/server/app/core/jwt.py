from datetime import datetime, timedelta
from typing import Union, Any

from jose import jwt
from app.core.settings import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY


def createAccessToken(
    *, data: dict, subject: Union[str, Any], expires_delta: timedelta = None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "sub": str(subject)})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
