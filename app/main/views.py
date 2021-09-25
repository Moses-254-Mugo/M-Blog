from flask import render_template,request, redirect, url_for,abort

from app import quotes
from . import main
from .forms import ReviewForm, UpdateProfile
from flask_login import login_required, current_user
from ..models import User
from .. import db,photos
import markdown2  
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

@main.route('/new_blogs', method=['GET', 'POST'])
@login_required
def new_blogs():
    form = BlogsForm()
    if form

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)