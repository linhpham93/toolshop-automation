class Login_page():
    def __init__(self, page):
        self.page = page
        self.email_locator = page.get_by_role("textbox", name="Email address *")
        self.password_locator = page.get_by_role("textbox", name="password*")
        self.login_btn = page.get_by_role("button", name="Login")
        
    def login(self, email, password):
        self.page.goto("auth/login")
        self.email_locator.fill(email)
        self.email_locator.fill(password)
        self.login_btn.click()