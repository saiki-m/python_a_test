import pathlib
from flask import Flask
from . import database, user

def create_app():
    app = Flask(
        __name__,
        instance_path=pathlib.Path().resolve()/'data',
        instance_relative_config=True
    )
    app.config.from_pyfile('config.py')
    app.teardown_appcontext(database.close_db)
    app.register_blueprint(user.bp)

    @app.route('/')
    def index():
        return 'Index Page'

    return app