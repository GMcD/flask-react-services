from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_redis import FlaskRedis

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
r = FlaskRedis()
login = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('api.config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
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
