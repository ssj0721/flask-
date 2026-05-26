from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_pydantic_spec import FlaskPydanticSpec
from flask_migrate import Migrate
from flask_mail import Mail
from flask_redis import FlaskRedis

# 注册数据库
db = SQLAlchemy()
# 注册Redis
redis_client = FlaskRedis(decode_responses=True)
# 注册数据库迁移
migrate = Migrate()
# 注册jwt
jwt = JWTManager()
# 注册邮箱
mail = Mail()
# 注册接口文档
spec = FlaskPydanticSpec(
    'flask',
    title='GCOJ',
    version='v1.0'
)