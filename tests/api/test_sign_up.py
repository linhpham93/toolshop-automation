from rich import print

def test_sign_up_success(api, random_email):
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
                "password": "Supessaaar111Secure@123",
                "email": random_email
    }
    response = api.post(
        "users/register",
        data = payload
    )
    print(response.json())
    assert response.status == 201

    
def test_login_success(api, create_account):
    payload = {
        "email": create_account["email"],
        "password": create_account["password"]
    }
    response = api.post("users/login", data=payload)
    print (response.json())
    assert response.status == 200