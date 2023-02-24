from flask import render_template, request, Blueprint
from flask_login import LoginManager, current_user
from project.models import Job

# similar to the app.route change it, name thing.
main = Blueprint('main', __name__)

@main.route('/')
def index():
    jobs = Job.query.filter_by(is_active=True).all()
    return render_template('index.html', jobs=jobs)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
