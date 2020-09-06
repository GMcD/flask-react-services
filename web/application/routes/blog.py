"""
    Simple Blog Post CRUD routes.
"""
from flask import render_template, request, url_for, flash, redirect
from flask import current_app as app
from web.application.models import db, Post
from werkzeug.exceptions import abort

def get_post(post_id):
    """ Get Post instance from post_id or throw 404 """
    instance = Post.query.filter_by(id=post_id).first()
    if not instance:
        abort(404)
    return instance

@app.route('/')
@app.route('/blog/')
def index():
    """ display list of Post instances ordered by id """
    posts = Post.query.order_by('id').all()
    return render_template('index.html', posts=posts)

@app.route('/blog/<int:post_id>')
def post(post_id):
    """ display individual Post instance """
    instance = get_post(post_id)
    return render_template('post.html', post=instance)

@app.route('/blog/create', methods=('GET', 'POST'))
def create():
    """ render Post Create form, and create Post """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            instance = Post(title=title, content=content)
            db.session.add(instance)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/blog/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    """ render Post Edit form, and update Post """
    instance = get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            instance.title = title
            instance.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=instance)

@app.route('/blog/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    """ delete Post instance """
    instance = get_post(post_id)
    db.session.delete(instance)
    db.session.commit()
    flash('"{}" was successfully deleted!'.format(instance.title))
    return redirect(url_for('index'))
