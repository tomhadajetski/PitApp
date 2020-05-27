from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Tom'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)