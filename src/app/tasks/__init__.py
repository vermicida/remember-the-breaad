from flask import Response
from json import dumps


def create_response(data, status=200):
    options = {
        'response': None if data is None else dumps(data),
        'headers': {'Content-Type': 'application/json'},
        'status': status
    }
    return Response(**options)
