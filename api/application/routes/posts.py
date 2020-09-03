import time
from flask import current_app as app
from ..models import Post
from ..schemas import PostSchema

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/posts")
def posts():
    all_posts = Post.query.all()
    return { 'posts' : posts_schema.dump(all_posts) }

@app.route("/posts/<post_id>")
def post_detail(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return post_schema.dump(post)
