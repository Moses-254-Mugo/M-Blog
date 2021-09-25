from flask import render_template,request, redirect, url_for
from . import main
from .forms import ReviewForm
from flask_login import login_required



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Home - Hello Moses...'
    return render_template('index.html', message = message)