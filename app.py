from project import create_app
from project.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run()
