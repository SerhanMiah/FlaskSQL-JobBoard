from flask import Flask, render_template
from job_board.routes import job_board
from flask_login import LoginManager, current_user

app = Flask(__name__)
app.register_blueprint(job_board)

app.config['SECRET_KEY'] = 'your-secret-key'

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    # TODO: Load and return user from the database based on user_id
    return None

@login_manager.unauthorized_handler
def unauthorized():
    # Redirect to the login page if user is not authorized
    return render_template('login.html')

@app.route('/')
def index():
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = None
    return render_template('index.html', username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: handle login form submission
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # TODO: handle registration form submission
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
