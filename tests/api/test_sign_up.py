from rich import print

def test_sign_up_with_body_empty (api):
    payload = {
    }
    response = api.post("users/register", data=payload)
    assert response.status == 422
    assert response.json()["first_name"] == ['The first name field is required.']
    assert response.json()["last_name"] == ['The last name field is required.']
    assert response.json()["email"] == ['The email field is required.']
    assert response.json()["password"] == ['The password field is required.']

def test_login_success(api, create_account):
    payload = {
        "email": create_account["email"],
        "password": create_account["password"]
    }
    response = api.post("users/login", data=payload)
    assert response.status == 200
    assert response.json()["access_token"]
 
    
def test_login_failed (api):
    payload = {
        "email": "nobody.invalid@example.com",
        "password": "wrong-password-1"
    }
    response = api.post("users/login", data=payload)
    assert response.status == 401
    assert response.json()["error"] == "Unauthorized"