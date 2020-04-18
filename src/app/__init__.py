from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()
ma = Marshmallow()


def create_app():

    # Create and configure the app.
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    CORS(app)

    # Initialize database connector and parser.
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        # Register the blueprints.
        from app.landing.routes import landing_bp
        from app.tasks.routes import tasks_bp
        from app.utils.routes import utils_bp
        app.register_blueprint(landing_bp)
        app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
        app.register_blueprint(utils_bp, url_prefix='/api/utils')

        # Create the tables with a crappy way to
        # handle if they are already created.
        try:
            db.create_all()
        except OperationalError as err:
            print(err)
            if err.code != 1050:
                raise err
        return app
