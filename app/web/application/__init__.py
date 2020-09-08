import os
from celery import Celery

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
celery = Celery()
toolbar = DebugToolbarExtension()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('web.config.DevConfig')

    from web.blueprints.auth import bp as auth_bp
    from web.application.errors import bp as errors_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login.init_app(app)
    login.login_view = 'login'
    toolbar.init_app(app)

    # clry = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    with app.app_context():
        # Register Blueprints

        # Include our Routes
        from web.application.routes import blog, email
        db.create_all()

        return app
