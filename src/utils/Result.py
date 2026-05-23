from pydantic import BaseModel
from flask import json


class Result(BaseModel):
    code: int
    msg: str
    data: object

    def to_dict(self):
        return self.model_dump()

    @staticmethod
    def success(data=None):
        result = Result(
            code=1,
            msg='success',
            data=data
        )
        return result.model_dump()

    @staticmethod
    def error(msg: str = "操作失败"):
        result = Result(
            code=0,
            msg=msg,
            data=None
        )
        return result.model_dump()