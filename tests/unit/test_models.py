from db.db import Member

def test_new_member():
    """
    Given a new member
    Confirm when a new member is created
    And check for properly defined fields
    """
    member = Member('John', 'Smith', '1/1/2000', 'MX')
    assert member.first_name == 'John'
    assert member.last_name == 'Smith'
    assert member.dob == '1/1/2000'
    assert member.country == 'MX'