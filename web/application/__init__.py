import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('web.config.DevConfig')

    from web.blueprints.auth import bp as auth_bp
    from .errors import bp as errors_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'login'

    with app.app_context():
        # Register Blueprints

        # Include our Routes
        from . import routes
        db.create_all()

        return app
