from playwright.sync_api import Page, expect
import time

def test_show_9_items(home_page):
    expect(home_page.product_item).to_have_count(9)

def test_search_product(home_page):
    home_page.search_product("pliers")
    expect(home_page.page.locator('[data-test="search_completed"]')).to_be_visible()
    names = home_page.product_item.all_inner_texts()
    for key in names:
        assert key != []
        assert "pliers" in key.lower()

def test_sort_low_to_high(home_page):
    home_page.sort_low_to_high()
    expect(home_page.page.locator('[data-test="sorting_completed"]')).to_be_visible()
    prices = home_page.product_price.all_inner_texts()
    numbers = [float(text.replace("$", "")) for text in prices]
    assert numbers == sorted(numbers, reverse=False)