from rich import print

def test_get_product_list(api):
    response_product_list = api.get("products?page=1")
    product_id = response_product_list.json()["data"][0]["id"]
    
    response_product_detail = api.get(f"products/{product_id}")
    print(response_product_detail.json())
    assert response_product_detail.status == 200
    assert response_product_detail.json()["id"] == product_id
    assert response_product_detail.json()["price"] > 0
    expected_keys = ["id", "name", "price", "in_stock", "category", "brand"]
    body = response_product_detail.json()
    for key in expected_keys:
        assert key in body