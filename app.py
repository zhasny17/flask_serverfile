from core import create_app
import os
import json
from flask import g


def populate_env():
    try:
        with open('config.json', 'r') as f:
            json_schema = json.load(f)
            os.environ['KOPA_LIVE_DOMAIN'] = json_schema.get('KOPA_LIVE_DOMAIN')
            os.environ['SERVER_NAME'] = json_schema.get('SERVER_NAME')
    except FileNotFoundError:
        print('####### Arquivo de configuracao necessario')


populate_env()
print('!!!! Variaveis de ambiente criadas')
application=create_app()
application.run()