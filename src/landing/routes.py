from flask import Blueprint, render_template

landing_bp = Blueprint('landing_bp', __name__, template_folder='templates')


@landing_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
