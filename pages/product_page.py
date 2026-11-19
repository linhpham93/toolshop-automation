class ProductPage():
    def __init__(self, page):
        self.page = page
        self.product_name = page.locator('[data-test="product-name"]')
        self.product_unit_price = page.locator('[data-test="unit-price"]')
        self.add_to_cart_btn = page.get_by_role("button", name="Add to cart")
        self.quantity_cart = page.locator('[data-test="cart-quantity"]')

    def open_product_detail(self, id):
        self.page.goto(f"product/{id}")
    
    def add_item_to_cart(self):
        self.add_to_cart_btn.click()