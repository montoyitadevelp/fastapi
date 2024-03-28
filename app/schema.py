from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class IgnoredType:
    pass


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserResponse(BaseModel):
    id: int
    name: str
    lastname: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        from_attributes = True

class VotesResponse(BaseModel):
    Post: PostResponse
    votes: int


class UserCreate(BaseModel):
    name: str
    lastname: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Votes(BaseModel):
    post_id: int
    dir: conint(le=1)
