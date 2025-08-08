from flask import render_template, current_app
from . import main

@main.route('/')
def index():
    posts = current_app.posts
    return render_template('index.html', posts=posts)