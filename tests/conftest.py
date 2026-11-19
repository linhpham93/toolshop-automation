import pytest
import uuid
from pages.home import HomePage
from pages.product_page import ProductPage
from playwright.sync_api import expect
from datetime import datetime
import time

API_URLS	 = {
    "https://practicesoftwaretesting.com": "https://api.practicesoftwaretesting.com",
    "https://with-bugs.practicesoftwaretesting.com" : "https://api-with-bugs.practicesoftwaretesting.com"
}

@pytest.fixture(scope="function")
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
def admin_token(api):
    payload_admin = {
     "email": "admin@practicesoftwaretesting.com",
    "password": "welcome01"
    }
    admin_login = api.post("users/login", data=payload_admin)
    print("Admin login")
    assert admin_login.status == 200
    token_admin = admin_login.json()["access_token"]
    return token_admin

@pytest.fixture
def user_info():
    first_name = uuid.uuid4().hex[8]
    email = f"{first_name}@example.com"
    infor = {
        "first_name" : first_name,
        "last_name" : "QA",
        "email" : email,
        "password" : "Supessaaar111Secure@123"
    }
    return infor    
    
@pytest.fixture
def create_account(api, user_info, admin_token):
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
    user_id = response.json()["id"]
    yield payload

    admin_delete_user = api.delete(
        f"users/{user_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
        )
    assert admin_delete_user.status == 204

@pytest.fixture
def clean_account(api, admin_token):
    list_account_id = []
    yield list_account_id
    for id in list_account_id:
        admin_delete_user = api.delete(
            f"users/{id}",
            headers={"Authorization": f"Bearer {admin_token}"}
        )
    assert admin_delete_user.status == 204

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

@pytest.fixture
def sort_low_to_high_result(home_page):
    home_page.sort_low_to_high()
    expect(home_page.page.locator('[data-test="sorting_completed"]')).to_be_visible()
    prices = home_page.product_price.all_inner_texts()
    numbers = [float(text.replace("$", "")) for text in prices]
    assert numbers == sorted(numbers)
    return numbers

def pytest_html_report_title(report):
    report.title = "Mini project Test Report"

def pytest_metadata(metadata, config):
    base_url = (config.getoption("base_url") or config.getini("base_url")).rstrip("/")
    metadata["Environment"] = "Practice site"
    metadata["Tester"] = "Linh"
    metadata["Base URL"] = base_url
    
