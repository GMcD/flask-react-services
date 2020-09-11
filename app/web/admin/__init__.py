"""
    Flash Application instance to serve API
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

# Globally accessible libraries
db = SQLAlchemy()
admin = Admin()

def create_app():
    """
        Initialize the Admin application.
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('web.config.DevConfig')

    from web.blueprints.admin import bp as admin_bp

    # Register Blueprints
    app.register_blueprint(admin_bp)

    # Initialize Plugins
    db.init_app(app)
    admin.init_app(app)

    with app.app_context():

        return app
