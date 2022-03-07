from flask import Flask
from .auth import db
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from os import path


bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'fhbhbghbg hreiuehfuhr'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:kimachas@localhost/pitch'
    db.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering Auth
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    # Initializing flask extensions
    bootstrap.init_app(app)

    from .models import User, Comment, Pitch
    create_database(app)

    # Will add the views and forms

    return app


def create_database(app):
    if not path.exists('app/' + 'pitch'):
        db.create_all(app=app)
        print('Created Database!')
