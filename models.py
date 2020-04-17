from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
import hashlib

db = SQLAlchemy()
migrate = Migrate(db=db)

tables_config = {
    'mysql_charset': 'utf8mb4',
}


def generate_uuid():
    return str(uuid.uuid4())


class Accounts(db.Model):
    __table_args__ = (
        tables_config
    )
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    api_key = db.Column(db.String(128), unique=True, nullable=False)

