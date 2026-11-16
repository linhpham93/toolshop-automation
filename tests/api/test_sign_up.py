

def test_login_success(api, create_account):
    payload = {
        "email": create_account["email"],
        "password": create_account["password"]
    }
    response = api.post("users/login", data=payload)
    assert response.status == 200
    print("User login")