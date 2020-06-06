from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Ready for some trivia!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'I know lots of dumb things!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

#----------------- Login -----------------------#
@app.route('/login', methods=['GET', 'POST'])
def login():

    # If user is already logged in, redirect to homepage
    if current_user.is_authenticated:
        return redirect(url_for(index))
    form = LoginForm()

    #queries db to check for username, then password
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.check_password(password=form.password.data):
            flash('Invalid username or password')
            return(redirect(url_for('index')))
        login_user(user, remember=form.remember_me.data)

        # After login, redirects to the page user was initially trying to access
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

#----------------- Logout -----------------------#
@app.route('/logout')
def logout():
    logout_user()
    return(redirect(url_for('index')))
