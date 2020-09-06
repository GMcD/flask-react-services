from flask import render_template, request, url_for, flash, redirect
from flask import current_app as app
from ..models import db, Post
from werkzeug.exceptions import abort

conn = db.session

def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    return post

@app.route('/')
@app.route('/blog/')
def index():
    posts = Post.query.order_by(id).all()
    return render_template('index.html', posts=posts)

@app.route('/blog/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/blog/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post = Post(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/blog/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/blog/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(post.title))
    return redirect(url_for('index'))
