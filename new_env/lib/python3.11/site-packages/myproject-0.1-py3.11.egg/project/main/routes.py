from flask import render_template, request, Blueprint
from flask_login import LoginManager, current_user
from project.models import Job
from datetime import datetime

# similar to the app.route change it, name thing.
main = Blueprint('main', __name__)

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    jobs = Job.query.order_by(Job.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', jobs=jobs)



@main.route("/about")
def about():
    return render_template('about.html', title='About')
