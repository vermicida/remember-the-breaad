import logging
import base64
import boto3
import json
import os
import sys
from botocore.exceptions import ClientError

REGION_NAME = os.getenv('REGION_NAME')
SECRET_NAME = os.getenv('SECRET_NAME')


def get_secret(secret_name):

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=REGION_NAME
    )

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        logging.error(f'Error trying to get the secret {secret_name}')
        logging.error(e.response['Error']['Code'])
        sys.exit(1)
    else:
        value = response['SecretString'] \
            if 'SecretString' in response \
            else base64.b64decode(response['SecretBinary'])
    return json.loads(value)


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@{host}/{db}'.format(**get_secret(SECRET_NAME))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
