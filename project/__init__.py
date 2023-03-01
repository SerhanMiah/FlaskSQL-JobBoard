from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from project.config import Config
from flask_assets import Environment, Bundle
from flask_scss import Scss


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
assets = Environment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    assets.init_app(app)
    Scss(app)

    js_bundle = Bundle('js/bootstrap.bundle.min.js', output='gen/packed.js')
    css_bundle = Bundle('css/bootstrap.css', 'scss/styles.scss', output='gen/packed.css')

    assets.register('js_bundle', js_bundle)
    assets.register('css_bundle', css_bundle)

    from project.users.routes import users
    from project.main.routes import main
    from project.job_board.routes import job_board
    from project.errors.handlers import errors
    from project.applicants.routes import applicants_bp

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(job_board)
    app.register_blueprint(applicants_bp)
    app.register_blueprint(errors)

    return app
