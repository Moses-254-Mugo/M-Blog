from flask import render_template,request, redirect, url_for,abort,flash
import flask_bootstrap

from app import quotes
from . import main
from .forms import CommentForm, ReviewForm, UpdateProfile
from flask_login import login_required, current_user
from ..models import Comment, User,Blog
from .. import db,photos
import markdown2  
from app.main.forms import BlogsForm
from app.quotes import get_quotes




# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to M-Blog Online Website'
    quotes = get_quotes()
    return render_template('index.html',title = title, quotes = quotes)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/new_blogs', methods=['GET', 'POST'])
@login_required
def new_blogs():
    form = BlogsForm()
    if form.validate_on_submit():
        blog = Blog(title= form.title.data, content=form.content.data, author=current_user)
        blog.save()
        flash('Your post has been created!', 'Success')
        return redirect(url_for('main.index'))
    return render_template("new_blogs.html", title='New Post', form=form, legend='New Post')

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blogs(id):
    blog = Blog.query.get_or_404(id)
    if blog.user != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()

@main.route('/del_comment/<int:comment_id>', methods=['GET', 'POST']) 
@login_required
def del_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if (comment.user.id) != current_user.id:
        abort(403)
    db.session.delete(comment)
    db.session.commit()

    # return redirect(url_for('main.'))

@main.route('/vew_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def view_comment(id):
    blog = Blog.query.get_or_404(id)
    blog_comment = Comment.query.filter_by(blog_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(blog_id=id, comment=comment_form.comment.data, user=current_user)
        new_comment.save_comment()
        
    return render_template('view_comment.html', blog=blog, blog_comments = blog_comment, comment_form= comment_form)
