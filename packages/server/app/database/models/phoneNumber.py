from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class PhoneNumber(Base):
    __tablename__ = "phoneNumbers"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"))
    phoneNumber = Column(String)
    user = relationship("User", back_populates="phoneNumbers")
