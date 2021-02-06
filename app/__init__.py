from flask import Flask
from .routes import *
from .cache import cache


def create_app():

    app = Flask(__name__)
    cache.init_app(app)
    app.register_blueprint(routes)

    return app
    