import re

from flask import Blueprint, request, jsonify, Response,abort
from src.extensions import spec,redis_client
from src.utils import Result,JwtUtil
from .schemas.User import EmailDTO, UserRegisterDTO, UserLoginDTO
from flask_pydantic_spec import Response, Request
from pydantic import BaseModel,constr,Field
from flask_jwt_extended import create_access_token,create_refresh_token,decode_token,jwt_required,get_jwt_identity,get_jwt
from src.service import CommentService,UserService
from src.utils.constants import ErrorMessage


auth = Blueprint('auth', __name__)


# 获取验证码
@auth.route('/verify',methods=['POST'])
@spec.validate(body=Request(EmailDTO), resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['auth'])
def getVerifyCode():
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email = request.json['email']
    if not re.match(email_pattern, email):
        abort(400,description=ErrorMessage.EMAIL_ERROR)
    UserService.sendVerifyCode(email)
    return Result.success("验证码发送成功!")


# 注册
@auth.route('/register',methods=['POST'])
@spec.validate(body=Request(UserRegisterDTO), resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['auth'])
def register():
    userRegisterDTO = UserRegisterDTO(**request.json)
    UserService.register(userRegisterDTO)
    return Result.success()


# 登录
@auth.route('/login',methods=['POST'])
@spec.validate(body=Request(UserLoginDTO), resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['auth'])
def login():
    userLoginDTO = UserLoginDTO(**request.json)
    userLoginVO = UserService.login(userLoginDTO)
    return Result.success(userLoginVO)



# 刷新令牌



# 退出
@auth.route('/refresh',methods=['POST'])
@spec.validate(resp=Response(HTTP_200=Result, HTTP_422=Result), tags=['auth'])
@jwt_required
def logout():
    user_id = get_jwt_identity()
    UserService.logout(user_id)
    return Result.success()


