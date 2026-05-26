from os import access

from flask_jwt_extended import create_access_token, create_refresh_token

from src.modules.auth.models.Role import RoleDB, UserRoleDB
from src.service import CommentService
from src import redis_client,db
from flask import abort
import random
from src.modules.auth.schemas.User import UserRegisterDTO, User, UserLoginDTO, UserLoginVO
from src.modules.auth.schemas.Role import Role
from src.modules.auth.models.User import UserDB
from src.utils import Argon2Util
from src.utils.constants import ErrorMessage
from sqlalchemy import or_

class UserService:

    @staticmethod
    def sendVerifyCode(email:str):
        verifyCode = str(random.randint(100000, 999999))

        redis_client.setex(f"user:{email}", 300, verifyCode)

        flag = CommentService.sendVirCodeMail(email, verifyCode)
        if not flag:
            abort(400,description=ErrorMessage.SEND_EMAIL_ERROR)


    @staticmethod
    def register(userRegisterDTO: UserRegisterDTO):
        code = redis_client.get(f"user:{userRegisterDTO.email}")
        if code != userRegisterDTO.verifyCode:
            abort(400,description=ErrorMessage.CODE_ERROR)

        flag = db.session.query(UserDB).filter(
            or_(
                UserDB.email == userRegisterDTO.email,
                UserDB.name == userRegisterDTO.name
            ),
            UserDB.is_delete == False
        ).first()

        if flag:
            abort(400,description=ErrorMessage.USER_EXIST)

        password = Argon2Util.encrypt_password(userRegisterDTO.password)

        user = UserDB(name=userRegisterDTO.name, email=userRegisterDTO.email, password=password,nick=userRegisterDTO.name)
        db.session.add(user)
        db.session.commit()

        userRole = UserRoleDB(user_id=user.id,role_id=Role.normal_role)
        db.session.add(userRole)
        db.session.commit()

        redis_client.delete(f"user:{userRegisterDTO.email}")



    @staticmethod
    def login(userLoginDTO: UserLoginDTO) -> UserLoginVO:
        user = db.session.query(UserDB).filter(
            or_(
                UserDB.email == userLoginDTO.username,
                UserDB.name == userLoginDTO.username
            ),
            UserDB.is_delete == False
        ).first()

        if user is None:
            abort(400,description=ErrorMessage.LOGIN_ERROR)
        flag = Argon2Util.verify_password(user.password, userLoginDTO.password)

        if not flag:
            abort(400,description=ErrorMessage.LOGIN_ERROR)

        role = db.session.query(RoleDB).join(
            UserRoleDB, RoleDB.id == UserRoleDB.role_id
        ).filter(
            UserRoleDB.user_id == user.id
        ).first()

        access_token = create_access_token(identity=user.id,additional_claims={"role":role.role})
        refresh_token = create_refresh_token(identity=user.id,additional_claims={"role":role.role})

        user.refresh_token = refresh_token
        db.session.commit()

        userLoginVO = UserLoginVO(
            user_id=user.id,
            name=user.name,
            nick=user.nick,
            access_token=access_token,
            refresh_token=refresh_token
        )

        return userLoginVO



    @staticmethod
    def logout(user_id: int):
        user = db.session.query(UserDB).filter(
            UserDB.id == user_id
        ).first()

        user.refresh_token = None
        db.commit()



