
from web.application import db
from .models import Post

def test_testing_config(application):
    assert application.config['TESTING']
    assert '_test' in application.config['SQLALCHEMY_DATABASE_URI']

def test_create_post(application):
    TITLE = 'Title 1'
    assert not Post.query.all()
    new_post = Post(title=TITLE, content='Content 1')
    db.session.add(new_post)
    db.session.commit()
    assert Post.query.count() == 1
    assert Post.query.first().title == TITLE

def test_delete_post(application):
    TITLE = 'Title 2'
    assert not Post.query.all()
    new_post = Post(title=TITLE, content='Content 2')
    db.session.add(new_post)
    db.session.commit()
    assert Post.query.count() == 1
    db.session.delete(new_post)
    assert Post.query.count() == 0

def test_recycle_database(application):
    TITLE = 'Title 2'
    assert not Post.query.all()
    new_post = Post(title=TITLE, content='Content 3')
    db.session.add(new_post)
    db.session.commit()
    assert Post.query.count() == 1
    assert Post.query.first().title == TITLE
