from pages.product_page import ProductPage
from playwright.sync_api import expect

def test_product_show_correct_info(home_page):
    product_name = home_page.product_item.first.inner_text()
    product_price = home_page.product_price.first.inner_text()

    home_page.product_item.first.click()
    product_page = ProductPage(home_page.page)
    expect(product_page.product_name).to_contain_text(product_name)
    expect(product_page.product_unit_price).to_contain_text(product_price.replace("$",""))
    assert "/product/" in product_page.page.url