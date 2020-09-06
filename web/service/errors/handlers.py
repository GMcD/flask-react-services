from flask import make_response, jsonify

from .. import db
from . import bp

def custom_error(message, status_code):
    return make_response(jsonify(message), status_code)

@bp.app_errorhandler(404)
def not_found_error(error):
    return custom_error('The requested resource was not found...', 404)

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return custom_error('Something went badly wrong with my internals!', 500)

@bp.app_errorhandler(502)
def internal_error(error):
    return custom_error('The upstream server is taking too long...', 502)
