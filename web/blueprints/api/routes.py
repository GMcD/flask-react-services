import time
from werkzeug.exceptions import abort

from web.application.models import Post

from . import bp
from .schemas import PostSchema

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@bp.route('/time')
def get_current_time():
    return {'time': int(time.time())}

@bp.route("/posts")
def posts():
    all_posts = Post.query.all()
    return { 'posts' : posts_schema.dump(all_posts) }

@bp.route("/posts/<post_id>")
def post_detail(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    return post_schema.dump(post)
