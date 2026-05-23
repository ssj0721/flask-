import os
from datetime import timedelta
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()


class Config:
    # 数据库 配置
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 规定字符集
    JSON_AS_ASCII = False
    JSONIFY_MIMETYPE = "application/json; charset=utf-8"
    RESTFUL_JSON = {"ensure_ascii": False}

    # JWT 配置
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))


class DevelopmentConfig(Config):
    DEBUG = True
    RESTX_MASK_SWAGGER = False


class ProductionConfig(Config):
    DEBUG = False
    RESTX_MASK_SWAGGER = True


# 环境映射
config_env = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig,
    'default': DevelopmentConfig
}