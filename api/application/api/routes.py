import time
from . import bp
from ..models import Post
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
    return post_schema.dump(post)
