
from web.application.models import Post
from web.service import ma

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
