from pydantic import BaseModel

from pydantic import BaseModel


class PhoneNumber(BaseModel):
    userId: str
    phoneNumber: str
