"""
    Custom 404, 500 and 502 pages. The actual `error` is not reported.
    Making tbis explicit is pythonic, and makes pylint happy.
"""
from flask import render_template
from flask import Blueprint

from web.application import db
from . import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    """ Friendly Resource Not Found template """
    del error
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    """ Friendly Internal Server Error template """
    del error
    db.session.rollback()
    return render_template('errors/500.html'), 500

@bp.app_errorhandler(502)
def bad_gateway(error):
    """ Friendly Bad Gateway Error template """
    del error
    db.session.rollback()
    return render_template('errors/502.html'), 502
