"""Data models."""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login

class User(UserMixin, db.Model):
    """Data model for user accounts."""

    __tablename__ = 'reflask_users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    google = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(256),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    bio = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    avatar = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )
    password_hash = db.Column(
        db.String(128),
        index=False,
        unique=True,
        nullable=True
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):
    """Data model for blog posts."""

    __tablename__ = 'reflask_posts'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(128),
        index=False,
        unique=True,
        nullable=False
    )
    content = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
