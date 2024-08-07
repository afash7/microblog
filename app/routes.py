from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Afash'}
    posts = [
        {
            'author': {'username': 'Sadegh'},
            'body': 'Beautiful day in Narmak!'
        },
        {
            'author': {'username': 'Ahoora'},
            'body': 'im gay!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)