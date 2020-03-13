from app.common import create_response
from flask import Blueprint
from requests import get
from requests.exceptions import RequestException

utils_bp = Blueprint('utils_bp', __name__, template_folder='templates')


@utils_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return create_response({'status': 'Remember The Bread is up and running'})


@utils_bp.route('/ipv4', methods=['GET'])
def get_ipv4():
    try:
        r = get('http://169.254.169.254/latest/meta-data/public-ipv4', timeout=3)
    except RequestException:
        ipv4 = 'IP desconocida'
    else:
        ipv4 = r.text if r.status_code == 200 else 'IP desconocida'
    return create_response({'ipv4': ipv4})
