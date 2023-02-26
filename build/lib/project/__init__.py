from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from project.config import Config
from sass import compile
# from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    # Bootstrap(app)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    
    from project.users.routes import users
    from project.main.routes import main
    from project.job_board.routes import job_board
    from project.errors.handlers import errors
    # Move the import inside the create_app function
    from project.applicants.routes import applicants_bp


    
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(job_board)
    app.register_blueprint(applicants_bp)
    app.register_blueprint(errors)

    return app
