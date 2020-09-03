import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_redis import FlaskRedis
from oauthlib.oauth2 import WebApplicationClient

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
r = FlaskRedis()
login = LoginManager()

# OAuth 2 client setup
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
google_client = WebApplicationClient(GOOGLE_CLIENT_ID)

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('api.config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    r.init_app(app)
    login.init_app(app)
    login.login_view = 'login'

    with app.app_context():
        # Include our Routes
        from . import routes
        db.create_all()

        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        return app
