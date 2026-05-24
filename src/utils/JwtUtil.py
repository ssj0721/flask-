from flask_jwt_extended import create_access_token,create_refresh_token,decode_token,jwt_required,get_jwt_identity,get_jwt
from functools import wraps
from src.utils.Result import Result

class JwtUtil:
    def admin_required(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            if get_jwt().get("role") != "admin":
                return Result.error("权限不够")
            return fn(*args, **kwargs)

        return wrapper

    def user_required(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            if get_jwt().get("role") != "user":
                return Result.error("权限不够")
            return fn(*args, **kwargs)

        return wrapper