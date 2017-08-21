from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config.from_pyfile('config.py')

mongo =PyMongo(app)

from app.home import home as home_blueprint
app.register_blueprint(home_blueprint)

from app.user import user as user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')

from app.master import master as master_blueprint
app.register_blueprint(master_blueprint, url_prefix='/master')
