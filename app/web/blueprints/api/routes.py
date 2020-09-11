import time
from flask import request
from flask_restful import Resource

from web.service import api
from web.application import db
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
    all_posts = Post.query.order_by('id').all()
    return { 'posts' : posts_schema.dump(all_posts) }

@bp.route("/posts/<post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return post_schema.dump(post)

class PostListResource(Resource):
    def get(self):
        posts = Post.query.order_by('id').all()
        return posts_schema.dump(posts)

    def post(self):
        new_post = Post(
            title=request.json['title'],
            content=request.json['content']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)

api.add_resource(PostListResource, '/v2/posts')

class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post_schema.dump(post)

    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'content' in request.json:
            post.content = request.json['content']

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204

api.add_resource(PostResource, '/v2/posts/<int:post_id>')
