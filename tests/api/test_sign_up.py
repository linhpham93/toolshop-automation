from rich import print

def test_a1_sign_up_success(api, user_info):  
    payload = {
                "first_name": "AABBCC",
                "last_name": "EEFFHH",
                "address": {
                    "street": "Street 1",
                    "house_number": "12",
                    "city": "City",
                    "state": "State",
                    "country": "Country",
                    "postal_code": "1234AA"
                },
                "phone": "0987654321",
                "dob": "1970-01-01",
                "password": user_info["password"],
                "email": user_info["email"]
    }
    response = api.post(
        "users/register",
        data = payload
    )
    assert response.status == 201
    
def test_a2_sign_up_with_body_empty (api):
    payload = {
    }
    response = api.post("users/register", data=payload)
    assert response.status == 422
    assert response.json()["first_name"] == ['The first name field is required.']
    assert response.json()["last_name"] == ['The last name field is required.']
    assert response.json()["email"] == ['The email field is required.']
    assert response.json()["password"] == ['The password field is required.']

def test_a3_login_success(api, create_account):
    payload = {
        "email": create_account["email"],
        "password": create_account["password"]
    }
    response = api.post("users/login", data=payload)
    assert response.status == 200
    assert response.json()["access_token"]
 
    
def test_a4_login_failed (api):
    payload = {
        "email": "nobody.invalid@example.com",
        "password": "wrong-password-1"
    }
    response = api.post("users/login", data=payload)
    assert response.status == 401
    assert response.json()["error"] == "Unauthorized"