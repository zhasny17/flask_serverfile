from flask import Blueprint, request, make_response, current_app
import models
from utils.error_handler import UnauthorizedException

bp = Blueprint('login', __name__)


def return_no_content():
    response = make_response('', 204)
    response.mimetype = current_app.config['JSONIFY_MIMETYPE']
    return response


@bp.route('/auth-proxy', methods=['GET'])
def auth():
    api_key = request.headers.get('x-api-key')
    if not api_key:
        raise UnauthorizedException(message='API KEY invalida')
    account = models.Accounts.query.filter_by(api_key=api_key).first()
    if not account:
        raise UnauthorizedException(message='API KEY invalida')
    print('!!! Conectado')
    return return_no_content()