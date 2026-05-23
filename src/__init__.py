from flask import Flask,jsonify
from src.extensions import jwt, db, spec, migrate
from src.utils import Result
from src.config import config_env
from src.modules.auth import auth


def create_app():
    app = Flask(__name__)

    app.config.from_object(config_env['dev'])

    # 全局异常处理
    @app.errorhandler(Exception)
    def handle_global_exception(e: Exception):
        print("error1")
        msg = getattr(e, 'description', str(e))
        return Result.error(msg)

    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    spec.register(app)

    app.register_blueprint(auth)


    return app
