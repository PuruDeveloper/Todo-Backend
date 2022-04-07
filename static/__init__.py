from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from static.logger_config import custom_logger


db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger('static')
logger = custom_logger(logger)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fkvtobdmbbuukp:4799b40e2781a5cc50577ec3a4b8817ce02e4e009794adc79f8bfadd103cac48@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d2mm0ovu6vbs9o'

    from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)

    from static.todoApp import todo_list
    app.register_blueprint(todo_list, url_prefix="/api/v1")

    return app
