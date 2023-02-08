from flask import Blueprint, request, jsonify, make_response, render_template

from db.db import Member, db

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/member_id', methods=['POST'])
def signup_member():
    """
    JSON Api endpoint to register new members. Purpose is to generate a unique member id. Example payload for a member looks like:
    {"id": 1, "first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}
    """
    data = request.get_json() 
    
    
    new_member = Member(first_name=data['first_name'], last_name=data['last_name'], dob=data['dob'], country=data['country'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'New member registered successfully'})

@auth_routes.route('/member_id/validate', methods=['GET', 'POST'])
def validate_member_id():
    """
    HTML Endpoint that creates a form which takes a member id as json and validates whether 
    it is a valid member id. If yes, return a success message; If not, returns error message.
    """
    if request.method == 'POST':
        id = request.form['content']
        try:
            current_member = Member.query.get_or_404(id)
            if current_member:
                return make_response(f'Successfully verified member id for {current_member.first_name} {current_member.last_name}!', 
                    200, {'message': 'Id has been successfully verified'}) 
        except:
            return make_response('member id is not valid. Try inputting a different member id and confirm member existence.'
                , 401, {'Message': 'Id could not be verified'}) 
    else:
        return render_template('validate.html')