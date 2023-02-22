from flask import Blueprint, render_template, request

job_board = Blueprint('job_board', __name__)

jobs = [
    {
        'title': 'Python Developer',
        'description': 'We are looking for an experienced Python developer to join our team.',
        'location': 'Remote',
        'salary': '60,000 - 80,000'
    },
    {
        'title': 'Frontend Developer',
        'description': 'We are looking for a skilled frontend developer to build beautiful and responsive user interfaces.',
        'location': 'San Francisco, CA',
        'salary': '80,000 - 100,000'
    },
    {
        'title': 'DevOps Engineer',
        'description': 'We are seeking a talented DevOps engineer to help us automate our infrastructure and deploy code quickly and reliably.',
        'location': 'New York, NY',
        'salary': '90,000 - 110,000'
    }
]

@job_board.route('/')
def index():
    return render_template('index.html', jobs=jobs)

@job_board.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        results = [job for job in jobs if keyword.lower() in job['title'].lower() or keyword.lower() in job['description'].lower()]
        return render_template('search_results.html', results=results)
    return render_template('search.html')

@job_board.route('/job/<int:job_id>')
def job(job_id):
    job = jobs[job_id]
    return render_template('job.html', job=job)
