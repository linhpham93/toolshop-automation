from rich import print
import pytest

@pytest.mark.api
def test_a1_sign_up_success(api, user_info, clean_account):  
    payload = {
                "first_name": user_info["first_name"],
                "last_name": user_info["last_name"],
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
    clean_account.append(response.json()["id"])

@pytest.mark.api 
def test_a2_sign_up_with_body_empty (api):
    payload = {
    }
    response = api.post("users/register", data=payload)
    assert response.status == 422
    assert response.json()["first_name"] == ['The first name field is required.']
    assert response.json()["last_name"] == ['The last name field is required.']
    assert response.json()["email"] == ['The email field is required.']
    assert response.json()["password"] == ['The password field is required.']

@pytest.mark.api
def test_a3_login_success(api, create_account):
    payload = {
        "email": create_account["email"],
        "password": create_account["password"]
    }
    response = api.post("users/login", data=payload)
    print(list(response.json().keys()))
    assert response.status == 200
    assert response.json()["access_token"]

@pytest.mark.api 
def test_a4_login_failed (api):
    payload = {
        "email": "nobody.invalid@example.com",
        "password": "wrong-password-1"
    }
    response = api.post("users/login", data=payload)
    assert response.status == 401
    assert response.json()["error"] == "Unauthorized"