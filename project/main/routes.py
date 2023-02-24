from flask import render_template, request, Blueprint
from flask_login import LoginManager, current_user

# similar to the app.route change it, name thing.
main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = None
    return render_template('index.html', username=username)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
