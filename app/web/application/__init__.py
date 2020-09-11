import os

# Celery Instance
from celery import Celery
celery = Celery(__name__, config_source='web.application.clrycfg')
from .clry import init_celery

# Flask Stuff
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
login = LoginManager()
toolbar = DebugToolbarExtension()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('web.config.DevConfig')

    from web.blueprints.auth import bp as auth_bp
    from web.application.errors import bp as errors_bp

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login.init_app(app)
    login.login_view = 'login'
    toolbar.init_app(app)

    with app.app_context():
        # Initialize Celery with Flask App context
        init_celery(app, celery=celery)

        # Include our Routes
        from web.application.routes import blog, email, progress
        from web.application.tasks import send_mail
        db.create_all()

        return app
