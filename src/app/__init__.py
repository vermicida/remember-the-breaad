from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


def create_app():

    # Create and configure the app.
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize database connector and parser.
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        # Register the blueprints.
        from app.landing.routes import landing_bp
        from app.tasks.routes import tasks_bp
        app.register_blueprint(landing_bp)
        app.register_blueprint(tasks_bp, url_prefix='/api/tasks')

        # Create the tables.
        db.create_all()

        return app
