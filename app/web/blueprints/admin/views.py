
from flask_admin.contrib.sqla import ModelView

from web.admin import admin, db
from web.application.models import User, Post

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
