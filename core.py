from flask import Flask
import os
from blueprints import videos, login
import utils


def create_app(config: dict = None) -> dict:
    ''' core function to create a app '''
    app = Flask(__name__)
    app.debug = False
    if config:
        app.config.from_mapping(**config)
    utils.error_handler.error_treatment(app=app)

    # NOTE cadastro blueprints
    app.register_blueprint(videos.bp)
    app.register_blueprint(login.bp)

    @app.after_request
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Methods'] = '*'
        header['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization, X-CSRF-TOKEN'
        return response

    return app
