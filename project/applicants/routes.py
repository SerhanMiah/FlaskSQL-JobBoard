from flask import Blueprint, render_template, redirect, url_for
from .forms import ApplicationForm
from project.models import Job, Application
from project import db
from flask_login import login_required

applicants_bp = Blueprint('applicants', __name__)

@applicants_bp.route('/apply/<int:job_id>', methods=['GET', 'POST'])
@login_required
def apply(job_id):
    job = Job.query.get_or_404(job_id)
    form = ApplicationForm()

    if form.validate_on_submit():
        application = Application(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            resume=form.resume.data,
            job_id=job.id
        )
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('jobs.job_detail', job_id=job.id))

    return render_template('apply.html', form=form, job=job)

@applicants_bp.route('/applications')
def application_list():
    applications = Application.query.all()
    return render_template('application_list.html', applications=applications)

@applicants_bp.route('/applications/<int:application_id>')
def application_detail(application_id):
    application = Application.query.get_or_404(application_id)
    return render_template('application_detail.html', application=application)
