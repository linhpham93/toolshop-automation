from playwright.sync_api import expect
from pages.login_page import LoginPage
from rich import print
import pytest

@pytest.mark.combined
def test_k1_login_succes(page, create_account):
    login_page =  LoginPage(page)
    login_page.open_page()
    login_page.sign_in(create_account["email"], create_account["password"])
    expect(login_page.page).to_have_url("/account")

@pytest.mark.combined
def test_k2_product_shows_correctly(product_detail_page, product_id):
    expect(product_detail_page.product_name).to_have_text(product_id["name"])
    price_product = float(product_detail_page.product_unit_price.inner_text())
    assert price_product == product_id["price"]

@pytest.mark.combined
def test_k3_add_to_cart(product_detail_page, api):
    product_detail_page.add_item_to_cart()
    expect(product_detail_page.quantity_cart).to_have_text("1")
    cart_id = product_detail_page.page.evaluate("sessionStorage.getItem('cart_id')")
    response = api.get(f"carts/{cart_id}")
    assert response.status == 200
    assert response.json()["cart_items"][0]["cart_id"] == cart_id
    assert response.json()["cart_items"][0]["quantity"] == 1

@pytest.mark.combined
def test_k4_search(api, home_page):
    keyword = "pliers"
    response = api.get(f"products/search?q={keyword}")
    search_result_api =[]
    for product in response.json()["data"]:
        search_result_api.append(product["name"])
        print(search_result_api)
    
    home_page.search_product(keyword)
    expect(home_page.page.locator('[data-test="search_completed"]')).to_be_visible()
    search_result_UI = home_page.product_item.all_inner_texts()
    print(search_result_UI)
    assert sorted(search_result_api) == sorted(search_result_UI)

@pytest.mark.combined
@pytest.mark.smoke   
def test_k5_sort_by_price(api, sort_low_to_high_result):
    response = api.get("products?sort=price,asc&page=1")
    assert response.status == 200
    price_api = []
    for product in response.json()["data"]:
        price_api.append(product["price"])
    assert price_api == sorted(price_api,  reverse=False)
    assert price_api == sort_low_to_high_result