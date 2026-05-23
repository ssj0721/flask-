from pydantic import BaseModel, Field, constr, StringConstraints
from typing import Annotated


class UserDTO(BaseModel):
    username: str
    password: str