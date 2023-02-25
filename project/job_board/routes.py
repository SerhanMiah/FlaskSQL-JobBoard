from flask import Blueprint, render_template, request, redirect, url_for, abort
from project import db
from project.models import Job, Application
from project.job_board.forms import JobForm

job_board = Blueprint('job_board', __name__)

@job_board.route('/')
def index():
    jobs = Job.query.filter_by(is_active=True).all()
    print(jobs)
    return render_template('index.html', jobs=jobs)

@job_board.route('/job_application/<int:app_id>')
def job_application(app_id):
    application = Application.query.get_or_404(app_id)
    return render_template('job_application.html', application=application)


@job_board.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        jobs = Job.query.filter(Job.title.ilike(f'%{keyword}%') | Job.description.ilike(f'%{keyword}%')).all()
        return render_template('search_results.html', jobs=jobs)
    return render_template('search.html')

@job_board.route('/job/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get(job_id)
    if not job:
        return abort(404)
    return render_template('job.html', job=job)


@job_board.route('/new_job', methods=['GET', 'POST'])
def new_job():
    form = JobForm()
    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            description=form.description.data,
            location=form.location.data,
            salary=form.salary.data
        )
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('job_board.index'))
    return render_template('new_job.html', form=form)
