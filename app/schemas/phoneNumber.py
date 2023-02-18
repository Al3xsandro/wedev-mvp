from pydantic import BaseModel

from pydantic import BaseModel
from typing import Optional


class PhoneNumber(BaseModel):
    userId: str
    phoneNumber: str


class PhoneNumberResponse(BaseModel):
    id: Optional[int] = None
    phoneNumber: str

    class Config:
        orm_mode = True
