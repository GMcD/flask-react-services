import pytest

from web.service import create_app, db

@pytest.fixture
def service():
    """
        Create web.service flask instance
            initialise Db and drop after yield
    """
    app = create_app()
    app.config.from_object('web.config.TestConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()  # looks like db.session.close() would work as well
        db.drop_all()
