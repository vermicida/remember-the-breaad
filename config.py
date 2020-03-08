import os


class Config:

    # General
    ENV = os.environ.get('FLASK_ENV') or 'development'
    DEBUG = os.environ.get('FLASK_DEBUG') or False

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql://MYSQL_USER:MYSQL_PASSWORD@MYSQL_HOST/MYSQL_DB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
