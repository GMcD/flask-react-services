"""
    Flask configuration
"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY', 'MY NOT SECRET KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME', 'COOKIE-NAME')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', 'NO-DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # set optional bootswatch theme
    FLASK_ADMIN_SWATCH = 'slate'

    # Google Configuration
    GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

    # Google Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get("MAIL_USERNAME", None)
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD", None)

    # Redis Broker for Celery
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    MAIL_SUPPRESS_SEND = False

class TestConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    MAIL_SUPPRESS_SEND = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "{}_test".format(Config.SQLALCHEMY_DATABASE_URI)
