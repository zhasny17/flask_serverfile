from flask import Blueprint, request
import models
from utils.error_handler import UnauthorizedException

bp = Blueprint('login', __name__)


@bp.route('/auth-proxy', methods=['GET'])
def auth():
    api_key = request.headers.get('x-api-key')
    if not api_key:
        raise UnauthorizedException(message='API KEY invalida')
    account = models.Accounts.quey.filter_by(api_key=api_key).first()
    if not account:
        raise UnauthorizedException(message='API KEY invalida')