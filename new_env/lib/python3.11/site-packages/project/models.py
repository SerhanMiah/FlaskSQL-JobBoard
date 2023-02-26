from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from project import db, login_manager
from flask_login import UserMixin
from flask import current_app
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id }).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
        # need to tell python its a static method

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# job class 
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary_min = db.Column(db.Integer)
    salary_max = db.Column(db.Integer)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    applicants = db.relationship('Application', backref='job', lazy=True)

    def __repr__(self):
        return f"Job(id={self.id}, title='{self.title}', company='{self.company}', location='{self.location}', salary_min='{self.salary_min}', salary_max='{self.salary_max}', date_posted='{self.date_posted}', is_active='{self.is_active}')"


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    resume = db.Column(db.String(255), nullable=False)
    date_applied = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='applications')

    def __repr__(self):
        return f"Application(id={self.id}, name='{self.name}', email='{self.email}', date_applied='{self.date_applied}')"
