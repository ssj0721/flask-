from datetime import datetime

from pydantic import BaseModel, Field, constr, StringConstraints
from typing import Annotated


class EmailDTO(BaseModel):
    email: str = Field(..., min_length=1)


class UserRegisterDTO(BaseModel):
    email: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)
    verifyCode: str = Field(..., min_length=1)


class UserLoginDTO(BaseModel):
    username: str = Field(..., min_length=1) # 可能为用户名或密码
    password: str = Field(..., min_length=1)


class UserLoginVO(BaseModel):
    access_token: str
    refresh_token: str
    user_id: int
    name: str
    nick: str



class User(BaseModel):
    id: int
    name: str
    niko: str
    email: str
    avatar_url: str
    password: str
    description: str
    refresh_token: str
    create_time: datetime
    update_time: datetime