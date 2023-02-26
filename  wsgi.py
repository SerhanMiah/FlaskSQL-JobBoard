import os
from project import create_app
from waitress import serve

app = create_app()


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
