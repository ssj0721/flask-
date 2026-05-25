from flask import Blueprint, request, jsonify, Response
from src.extensions import spec,redis_client
from .schemas.User import UserDTO
from src.utils import Result,JwtUtil
from .schemas.User import UserDTO
from flask_pydantic_spec import Response, Request
from pydantic import BaseModel,constr,Field
from flask_jwt_extended import create_access_token,create_refresh_token,decode_token,jwt_required,get_jwt_identity,get_jwt
from src.service import CommentService


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
@spec.validate(query=UserDTO, resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['api'])
def login():
    user = UserDTO(**request.args).model_dump()
    # jwt使用
    token = create_access_token(identity="2", additional_claims={"role":"user"})

    # # redis使用
    # redis_client.setex('user:123:name', 60, 'Alice')
    # name = redis_client.get('user:123:name')

    # password = ph.hash(user.password)

    # print(name)
    return Result.success({"token":token})


@auth.route('/refresh', methods=['POST'])
@spec.validate(resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['api'])
@JwtUtil.admin_required
def refresh():
    user_id = get_jwt_identity()
    role = get_jwt()['role']
    print(role)
    return Result.success(user_id)


@auth.route('/send', methods=['GET'])
@spec.validate(resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['api'])
def send_message():
    # mail使用
    op = CommentService.sendVirCodeMail("3115355853@qq.com","666345")
    if op:
        return Result.success("验证码已发送")
    else:
        return Result.error("获取验证码失败")


