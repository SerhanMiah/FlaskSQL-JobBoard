import os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from project import db
from flask_login import login_required, current_user
from datetime import datetime
from werkzeug.utils import secure_filename
from .forms import ApplicationForm
from project.models import Job, Application

# Remove this line
# app = create_app()

applicants_bp = Blueprint('applicants', __name__)

@applicants_bp.route('/apply/<int:job_id>', methods=['GET', 'POST'])
@login_required
def apply(job_id):
    job = Job.query.get(job_id)
    if job is None:
        flash('Invalid job ID', 'danger')
        return redirect(url_for('job_board.index'))

    form = ApplicationForm()
    if form.validate_on_submit():
        file = form.resume.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        application = Application(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            resume=filepath,
            date_applied=datetime.now(),
            job_id=job_id,
            user_id=current_user.id
        )
        db.session.add(application)
        db.session.commit()

        flash('Your application has been submitted', 'success')
        return redirect(url_for('job_board.index'))

    return render_template('apply.html', form=form, job=job)


@applicants_bp.route('/applications')
def application_list():
    applications = Application.query.all()
    return render_template('application_list.html', applications=applications)

@applicants_bp.route('/applications/<int:application_id>')
def application_detail(application_id):
    application = Application.query.get_or_404(application_id)
    return render_template('application_detail.html', application=application)

@applicants_bp.route('/my_applications')
@login_required
def my_applications():
    applications = Application.query.filter_by(user_id=current_user.id).all()
    return render_template('my_applications.html', applications=applications)
