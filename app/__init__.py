from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# from app import views, errors


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app Configurations
    app.config.from_object(config_options[config_name])


    # Initializing flask extension
    bootstrap.init_app(app)
    db.init_app(app)

    # Register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app