import os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from project import db
from flask_login import login_required, current_user
from datetime import datetime
from werkzeug.utils import secure_filename
from .forms import ApplicationForm
from project.models import Job, Application
from cloudinary.uploader import upload

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
        response = upload(file, cloud_name=current_app.config['CLOUDINARY_CLOUD_NAME'], api_key=current_app.config['CLOUDINARY_API_KEY'], api_secret=current_app.config['CLOUDINARY_API_SECRET'])
        file_url = response['secure_url']

        application = Application(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            resume=file_url,
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

@applicants_bp.route('/applications/<int:application_id>/delete', methods=['POST'])
@login_required
def delete_application(application_id):
    application = Application.query.get_or_404(application_id)
    if application.user_id != current_user.id:
        flash('You do not have permission to delete this application', 'danger')
        return redirect(url_for('applicants.my_applications'))

    db.session.delete(application)
    db.session.commit()

    flash('Application deleted successfully', 'success')
    return redirect(url_for('applicants.my_applications'))


@applicants_bp.route('/applications/<int:application_id>/update_status', methods=['GET', 'POST'])
@login_required
def update_application_status(application_id):
    application = Application.query.get_or_404(application_id)

    if application.user_id != current_user.id:
        flash('You do not have permission to update the status of this application', 'danger')
        return redirect(url_for('applicants.my_applications'))

    if request.method == 'POST':
        new_status = request.form.get('status')
        if new_status not in ['pending', 'approved', 'rejected']:
            flash('Invalid status', 'danger')
            return redirect(url_for('applicants.update_application_status', application_id=application_id))

        application.status = new_status
        db.session.commit()

        flash(f'Application status updated to {new_status}', 'success')
        return redirect(url_for('applicants.application_detail', application_id=application.id))

    return render_template('update_application_status.html', application=application)

