import os
from flask import Blueprint
from oauthlib.oauth2 import WebApplicationClient

# OAuth 2 client setup
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
google_client = WebApplicationClient(GOOGLE_CLIENT_ID)

bp = Blueprint('auth', __name__, template_folder='templates')

from .routes import *
