from flask import Flask,jsonify
from src.extensions import jwt, db, spec, migrate,mail,redis_client
from src.utils import Result
from src.config import config_env
import redis

def create_app():
    app = Flask(__name__)

    app.config.from_object(config_env['dev'])

    redis_client.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    spec.register(app)
    mail.init_app(app)

    from src.modules.auth import auth
    app.register_blueprint(auth)


    # 全局异常处理
    @app.errorhandler(Exception)
    def handle_global_exception(e: Exception):
        msg = getattr(e, 'description', str(e))
        return Result.error(msg)


    return app
