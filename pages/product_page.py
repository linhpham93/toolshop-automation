class ProductPage():
    def __init__(self, page):
        self.page = page
        self.product_name = page.locator('[data-test="product-name"]')
        self.product_unit_price = page.locator('[data-test="unit-price"]')
        self.add_to_cart_btn = page.locator('[class="btn-group mt-2"]')