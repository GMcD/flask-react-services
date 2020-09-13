import pytest

from web.application import create_app, db

# from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database
#
# def create_test_db(db_url):
#     engine = create_engine(db_url)
#     if not database_exists(engine.url):
#         create_database(engine.url)
#     print(database_exists(engine.url))

@pytest.fixture
def application():
    """
        Create web.application flask instance,
            initialise Db and drop after yield
    """
    app = create_app()
    app.config.from_object('web.config.TestConfig')

    # db_url = app.config['SQLALCHEMY_DATABASE_URI']
    # create_test_db(db_url)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
