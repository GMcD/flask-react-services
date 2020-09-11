from flask import Blueprint

bp = Blueprint('admin2', __name__)

from . import views
