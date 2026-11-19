from playwright.sync_api import Page, expect
import time

def test_u1_show_9_items(home_page):
    expect(home_page.product_item).to_have_count(9)

def test_u2_search_product(home_page):
    home_page.search_product("pliers")
    expect(home_page.page.locator('[data-test="search_completed"]')).to_be_visible()
    names = home_page.product_item.all_inner_texts()
    for key in names:
        assert key != []
        assert "pliers" in key.lower()

def test_u3_sort_low_to_high(sort_low_to_high_result):
    assert sort_low_to_high_result == sorted(sort_low_to_high_result, reverse=False)