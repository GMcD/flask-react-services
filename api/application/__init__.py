import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_redis import FlaskRedis

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
r = FlaskRedis()
login = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('api.config.DevConfig')

    from .errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from .api import bp as api_bp
    app.register_blueprint(api_bp)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    r.init_app(app)
    login.init_app(app)
    login.login_view = 'login'

    with app.app_context():
        # Register Blueprints

        # Include our Routes
        from . import routes
        db.create_all()

        return app
