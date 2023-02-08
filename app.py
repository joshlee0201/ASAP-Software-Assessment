from flask import Flask
import os
from db.db import db, Member

from config import SECRET_KEY
from auth import auth_routes


basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from db import db
    db.init_app(app)

    from auth import auth_routes
    app.register_blueprint(auth_routes)

    return app

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'account_storage.db')

db.init_app(app)

@app.route('/')
def index():
    return 'Hello World'


# @app.route('/members', methods=['GET'])
# def show_all_members():
#     members = Member.query.all()
#     result = []  
#     for member in members:  
#        member_data = {}  
#        member_data['first_name'] = member.first_name
#        member_data['last_name'] = member.last_name
#        member_data['dob'] = member.dob
#        member_data['country'] = member.country
#        result.append(member_data) 
#     return result

app.register_blueprint(auth_routes)
## signup POST

## validate GET POST