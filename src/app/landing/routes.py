from flask import Blueprint, render_template, Response
from requests import get

landing_bp = Blueprint('landing_bp', __name__, template_folder='templates')


@landing_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@landing_bp.route('/ipv4', methods=['GET'])
def get_ipv4():
    r = get('http://169.254.169.254/latest/meta-data/public-ipv4')
    options = {
        'response': r.text if r.status_code == 200 else 'IP desconocida',
        'headers': {'Content-Type': 'text/plain'},
        'status': 200
    }
    return Response(**options)
