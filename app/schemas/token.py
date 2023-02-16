from pydantic import BaseModel
from typing import Optional


class TokenSchema(BaseModel):
    access_token: str
    token_type: Optional[str]


class TokenPayload(BaseModel):
    sub: Optional[int] = None
