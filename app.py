from core import create_app
import os
import json


def populate_env():
    try:
        with open('config.json', 'r') as f:
            json_schema = json.load(f)
            os.environ['DB_CONNECTOR'] = json_schema.get('DB_CONNECTOR')
            os.environ['DB_USERNAME'] = json_schema.get('DB_USERNAME')
            os.environ['DB_PASSWORD'] = json_schema.get('DB_PASSWORD')
            os.environ['DB_HOST'] = json_schema.get('DB_HOST')
            os.environ['DATABASE'] = json_schema.get('DATABASE')
            os.environ['HOST_IP'] = json_schema.get('HOST_IP')
    except FileNotFoundError:
        print('####### Arquivo de configuracao necessario')



populate_env()
print('!!!! Variaveis de ambiente criadas')
application=create_app()
application.run()