from flask import render_template
from . import main
from .forms import LoginForm
from flask_login import login_required

#views
@main.route('/')
def index():

    '''
    View of root page function that returns the index page and its data
    '''
    return render_template('index.html')

# @main.route('/login')
# def login():

#     '''
#     View of root page function that returns the login page and its data
#     '''
#     return render_template('login.html')

# @main.route('/register')
# def register():

#     '''
#     View of root page function that returns the registration page and its data
#     '''
#     return render_template('register.html')