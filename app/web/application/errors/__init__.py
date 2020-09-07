"""
    Custom HTTP error pages, handling 404, 500, 502.
"""
from flask import Blueprint

bp = Blueprint('errors', __name__)

from . import handlers
