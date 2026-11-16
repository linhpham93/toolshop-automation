import pytest
import uuid

API_URLS	 = {
    "https://practicesoftwaretesting.com": "https://api.practicesoftwaretesting.com",
    "https://with-bugs.practicesoftwaretesting.com" : "https://api-with-bugs.practicesoftwaretesting.com"
}
   
@pytest.fixture(scope="session")
def base_url(pytestconfig):
    url = (pytestconfig.getoption("base_url") or pytestconfig.getini("base_url")).rstrip("/")
    return url

@pytest.fixture(scope="session")
def api_url(base_url):
    url = API_URLS[base_url]
    return url

@pytest.fixture
def api(playwright, api_url):
    context = playwright.request.new_context(base_url = api_url)
    yield context
    context.dispose()
    

def random_email():
    name = uuid.uuid4().hex[8]
    email = f"{name}@example.com"
    return email    
    
@pytest.fixture
def create_account(api):
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
                "email": f"{random_email}"
    }
    response = api.post(
        "users/register",
        data = payload
    )
    assert response.status == 201
    yield payload