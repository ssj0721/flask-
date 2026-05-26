from typing import ClassVar
from pydantic import BaseModel


class Role(BaseModel):
    id: int
    role: str

    normal_role: ClassVar[int] = 1

class RoleUser(BaseModel):
    id: int
    role_id: int
    user_id: int