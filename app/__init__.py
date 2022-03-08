from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_options
from os import path


bootstrap = Bootstrap()
db = SQLAlchemy()  # database object
migrate = Migrate(db)


def create_app(config_name):

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'fhbhbghbg hreiuehfuhr'
    db.init_app(app)
    # Initializing flask extensions
    bootstrap.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering Auth
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Comment, Pitch

    return app
