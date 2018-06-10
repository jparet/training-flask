# coding: utf-8

from flask import Blueprint, render_template, request

from flaskblog.models import Post


main = Blueprint('main', __name__)


@main.route('/about')
def about():
    """About page of the app."""
    return render_template('about.html', title='About')


@main.route('/')
@main.route('/home')
def home():
    """Home page of the app."""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
