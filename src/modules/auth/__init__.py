from flask import Blueprint, request, jsonify, Response
from src.extensions import spec
from .schemas.User import UserDTO
from src.utils import Result
from .schemas.User import UserDTO
from flask_pydantic_spec import Response, Request
from pydantic import BaseModel,constr,Field

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
@spec.validate(query=UserDTO, resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['api'])
def login():
    user = UserDTO(**request.args).model_dump()
    print(user)
    return Result.success(user)
