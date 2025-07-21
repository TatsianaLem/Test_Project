from pydantic import BaseModel, EmailStr
from typing import Optional



class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True



class OrderBase(BaseModel):
    title: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    user_id: int


class OrderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class OrderOut(OrderBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
