class LoginPage():
    def __init__(self, page):
        self.page = page
        self.email_field = page.get_by_role("textbox", name="Email address *")
        self.password_field = page.get_by_role("textbox", name="Email address *")
        self.login_btn = page.get_by_role("button", name="Login")

    def open_page(self):
        self.page.goto("/auth/login")

    def sign_in(self, email, password):
        self.email_field.fill(email)
        self.password_field(password)
        self.login_btn.click()