from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
import os
from os import path
from flask_uploads import UploadSet, configure_uploads, IMAGES


bootstrap = Bootstrap()
db = SQLAlchemy()  # database object
migrate = Migrate()
login_manager = LoginManager()
UPLOAD_FOLDER = 'static/uploads/'
photos = UploadSet('photos', IMAGES)
mail = Mail()

# provides different security levels and by setting it to strong will monitor the changes in a user's request header and log the user out.
login_manager.session_protection = 'strong'


def create_app(config_name):

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'fhbhbghbg hreiuehfuhr'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:kimachas@localhost/pitch'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # configure UploadSet
    configure_uploads(app, photos)

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
