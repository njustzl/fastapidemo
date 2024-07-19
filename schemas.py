from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    # image: File
    email: str
    # birthday: DateTime


class UserCreate(UserBase):
    phone: str


class User(UserBase):
    id: int
    is_emergency: bool

    class Config:
        orm_mode = True
