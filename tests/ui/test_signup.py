from pages.singup_page import SignupPage
from playwright.sync_api import expect

def test_register_failed(page):
    auth_page = SignupPage(page)
    auth_page.open_page()
    auth_page.register_button.click()
    expect(auth_page.first_name_error).to_contain_text("First name is required")
    expect(auth_page.last_name_error).to_contain_text("Last name is required")
    expect(auth_page.email_name_error).to_contain_text("Email is required")
    expect(auth_page.password_name_error).to_contain_text("Password is required")
