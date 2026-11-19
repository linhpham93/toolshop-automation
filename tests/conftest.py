import pytest
import uuid
from pages.home import HomePage
from pages.product_page import ProductPage

API_URLS	 = {
    "https://practicesoftwaretesting.com": "https://api.practicesoftwaretesting.com",
    "https://with-bugs.practicesoftwaretesting.com" : "https://api-with-bugs.practicesoftwaretesting.com"
}

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    args = dict(browser_context_args)
    args["viewport"] = {"width": 1920, "height": 1080}
    return args
   
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
    
@pytest.fixture
def random_email():
    name = uuid.uuid4().hex[8]
    email = f"{name}@example.com"
    return email    
    
@pytest.fixture
def create_account(api, random_email):
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
    assert response.status == 201
    user_id = response.json()["id"]
    print("Create account")
    yield payload

    payload_admin = {
     "email": "admin@practicesoftwaretesting.com",
    "password": "welcome01"
    }
    admin_login = api.post("users/login", data=payload_admin)
    print("Admin login")
    assert admin_login.status == 200
    token_admin = admin_login.json()["access_token"]

    admin_delete_user = api.delete(
        f"users/{user_id}",
        headers={"Authorization": f"Bearer {token_admin}"}
        )
    assert admin_delete_user.status == 204
    print("Admin delected user")

@pytest.fixture
def home_page(page):
    home = HomePage(page)
    home.open_home_page()
    yield home

@pytest.fixture
def product_id(api):
    response_product_list = api.get("products?page=1")
    product_id = response_product_list.json()["data"][0]["id"]
    product_name = response_product_list.json()["data"][0]["name"]
    product_price = response_product_list.json()["data"][0]["price"]
    product_info = {
        "id" :  product_id,
        "name" : product_name,
        "price" : product_price
    }
    return product_info

@pytest.fixture
def product_detail_page(page, product_id):
    product_detail_page = ProductPage(page)
    product_detail_page.open_product_detail(product_id["id"])
    return product_detail_page