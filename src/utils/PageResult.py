from pydantic import BaseModel
from typing import List,Any


class PageResult(BaseModel):
    total: int
    records: List[Any]