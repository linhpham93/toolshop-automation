class SignupPage():
    def __init__(self, page):
        self.page = page
        self.first_name_error = page.locator('[id="first_name-error"]')
        self.last_name_error = page.locator('[id="last_name-error"]')
        self.email_name_error = page.locator('[id="email-error"]')
        self.password_name_error = page.locator('[id="password-error"]')
        self.register_button = page.get_by_role("button", name="Register")

    def open_page(self):
        self.page.goto("auth/register")