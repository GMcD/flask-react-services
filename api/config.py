"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY', 'MY NOT SECRET KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME', 'COOKIE-NAME')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    SQLALCHEMY_ECHO = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

    SQLALCHEMY_ECHO = True
