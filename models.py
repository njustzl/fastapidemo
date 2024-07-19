from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True, index=True)
    # image = Column(File)
    email = Column(String)
    # birthday = Column(DateTime)
    is_emergency = Column(Boolean, default=False)
