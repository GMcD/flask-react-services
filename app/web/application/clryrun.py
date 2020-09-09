from web.application import celery, create_app
from .clry import init_celery

app = create_app()
init_celery(app, celery)
