from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

# test_main.py
import pytest
from flask_jwt_extended import create_access_token,create_refresh_token,decode_token
from src import create_app
from src.utils import Argon2Util


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client, app.app_context():
        yield client




def test_argon(client):
    password = "123456"
    hash = Argon2Util.encrypt_password(password)

    print(hash)

    op = Argon2Util.verify_password(hash, password)

    print(op)