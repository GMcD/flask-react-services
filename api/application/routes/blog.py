from flask import render_template, request, url_for, flash, redirect
from flask import current_app as app
from ..models import db
from werkzeug.exceptions import abort

conn = db.session

def get_post(post_id):
    post = conn.execute('SELECT * FROM reflask_posts WHERE id = :id', { 'id' : post_id }).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
@app.route('/blog/')
def index():
    posts = conn.execute('SELECT * FROM reflask_posts').fetchall()
    conn.close()
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
            conn.execute('INSERT INTO reflask_posts (title, content) VALUES (:title, :content)',
                         { 'title' : title, 'content' : content })
            conn.commit()
            conn.close()
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
            conn.execute('UPDATE reflask_posts SET title = :title, content = :content'
                         ' WHERE id = :id',
                         { 'title' : title, 'content' : content, 'id' : id})
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/blog/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn.execute('DELETE FROM reflask_posts WHERE id = :id', { 'id' : id })
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
