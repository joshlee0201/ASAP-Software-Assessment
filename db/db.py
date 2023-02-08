from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g
import sqlite3

db = SQLAlchemy()

# Example Member account storage
# {"id": 1, "first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dob = db.Column(db.String(50))
    country = db.Column(db.String(2))
    
    def __init__(self, first_name, last_name, dob, country):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.country = country

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['account_storage.fb'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)