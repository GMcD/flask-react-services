import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('web.config.DevConfig')

    from web.blueprints.api import bp as api_bp
    from .errors import bp as errors_bp

    # Register Blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(errors_bp)

    # Initialize Plugins
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        return app
