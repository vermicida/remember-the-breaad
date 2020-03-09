import logging
import boto3
import os
import sys
from botocore.exceptions import ClientError


def _get_parameter(client, name):
    try:
        r = client.get_parameter(Name=name)
    except ClientError as e:
        logging.error(f'Error trying to get the parameter {name}')
        logging.error(e.response['Error']['Code'])
        sys.exit(1)
    return r['Parameter']['Value']


_ssm = boto3.client('ssm')
_user = _get_parameter(_ssm, 'MYSQL_USER')
_pass = _get_parameter(_ssm, 'MYSQL_PASSWORD')
_host = _get_parameter(_ssm, 'MYSQL_HOST')
_ddbb = _get_parameter(_ssm, 'MYSQL_DB')


class Config:
    ENV = os.environ.get('FLASK_ENV') or 'development'
    DEBUG = os.environ.get('FLASK_DEBUG') or False
    SQLALCHEMY_DATABASE_URI = f'mysql://{_user}:{_pass}@{_host}/{_ddbb}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
