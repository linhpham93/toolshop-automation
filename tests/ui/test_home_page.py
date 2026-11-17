from pages.home import HomePage
from playwright.sync_api import Page, expect

def test_show_9_items(page):
    home_page = HomePage(page)
    home_page.open_home_page()
    expect(home_page.page).to_have_url("https://practicesoftwaretesting.com/") 
