from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_succes(page, create_account):
    login_page =  LoginPage(page)
    login_page.open_page()
    login_page.sign_in(create_account["email"], create_account["password"])
    expect.page.to_have_url("/account")
