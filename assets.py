from flask_assets import Environment, Bundle
from project import create_app

app = create_app()
assets = Environment(app)

sass_bundle = Bundle('scss/*.scss', filters='scss', output='gen/all.css')


assets.register('sass_all', sass_bundle)
