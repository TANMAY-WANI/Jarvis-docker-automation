from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        # Import routes
        from . import routes

        return app
