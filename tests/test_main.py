from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

# test_main.py
import pytest
from flask_jwt_extended import create_access_token,create_refresh_token,decode_token
from src import create_app

# 自动提供应用上下文的 fixture
@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client, app.app_context():
        yield client

# 测试用例直接使用 fixture