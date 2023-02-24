from flask import Blueprint, render_template, request, redirect, url_for
from project.models import db, Job
from project.job_board.forms import JobForm

job_board = Blueprint('job_board', __name__)

@job_board.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@job_board.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        results = Job.query.filter(Job.title.ilike(f'%{keyword}%') | Job.description.ilike(f'%{keyword}%')).all()
        return render_template('search_results.html', results=results)
    return render_template('search.html')

@job_board.route('/job/<int:job_id>')
def job(job_id):
    job = Job.query.get_or_404(job_id)
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
