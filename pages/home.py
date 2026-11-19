class HomePage():
    def __init__(self, page):
        self.page = page
        self.product_item = page.locator('[data-test="product-name"]')
        self.search_box = page.get_by_role("textbox", name="Search")
        self.search_btn = page.get_by_role("button", name="Search")
        self.sort_option = page.get_by_role("combobox", name="sort")
        self.product_price = page.locator('[data-test="product-price"]')

    def open_home_page(self):
        self.page.goto("")

    def search_product(self, product_name):
        self.search_box.fill(product_name)
        self.search_btn.click()

    def sort_low_to_high(self):
        self.sort_option.select_option(label="Price (Low - High)")
        