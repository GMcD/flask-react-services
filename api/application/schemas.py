
from . import ma
from .models import Post

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
