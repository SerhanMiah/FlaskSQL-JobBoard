from project import create_app
from project.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
