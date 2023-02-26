from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.errorhandler(403)
def forbidden():
    return render_template('errors/403.html'), 403

@errors.errorhandler(404)
def page_not_found():
    return render_template('errors/404.html'), 404

@errors.errorhandler(500)
def internal_server_error():
    return render_template('errors/500.html'), 500
