from flask import Blueprint, request, make_response, current_app
import requests
import os
from urllib.parse import urljoin
from utils.error_handler import UnauthorizedException

bp = Blueprint('login', __name__)

KOPA_LIVE_DOMAIN = os.environ.get()
session = requests.Session

def return_no_content():
    response = make_response('', 204)
    response.mimetype = current_app.config['JSONIFY_MIMETYPE']
    return response


@bp.route('/auth-proxy', methods=['GET'])
def auth():
    authorization = request.headers.get('Authorization')
    url = urljoin(KOPA_LIVE_DOMAIN, 'auth/me')
    res = session.get(url, headers={'Authorization': authorization})
    if res.ok:
        return return_no_content()
    else:
        raise UnauthorizedException(message='Token invalido')