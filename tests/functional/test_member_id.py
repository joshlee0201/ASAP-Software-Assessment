import auth

def test_member_validation(test_client):
    """
    Given an invalid member id
    When the Post request for /member_id/validate is submitted
    Then check for a valid response
    """
    response = test_client.post('/member_id/validate')
    assert response.status_code == 405
    assert b'member id is not valid. Try inputting a different member id and confirm member existence.' in response.data




def test_member_validation_form(test_client, captured_templates):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/my/view")
    assert response.status_code == 200

    assert len(captured_templates) == 1

    template, context = captured_templates[0]

    assert template.name == "validate.html"
