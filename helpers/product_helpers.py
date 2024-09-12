import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', 'products.json')
with open(file_path) as f:
    products = json.load(f)


def verify_product_details(product_id, locators):
    product_data = products.get(product_id)

    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found in product data")

    product_name = locators["name"].text_content().strip()
    product_price = locators["price"].text_content().replace("Rs. ", "").strip()
    product_category = locators["category"].text_content().replace("Category: ", "").strip()

    assert product_data[
               "name"] == product_name, f"Product name mismatch: Expected {product_data['name']}, got {product_name}"
    assert product_data[
               "price"] == product_price, f"Product price mismatch: Expected {product_data['price']}, got {product_price}"
    assert product_data[
               "category"] == product_category, f"Product category mismatch: Expected {product_data['category']}, got {product_category}"


def verify_cart_product_details(locators, product_id, quantity: int):
    product_data = products.get(product_id)

    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found in product data")

    product_name = locators["name"].text_content().strip()
    product_price = locators["price"].text_content().replace("Rs. ", "").strip()
    product_category = locators["category"].text_content().replace("Category: ", "").strip()
    product_quantity = locators["quantity"].text_content().strip()
    total_price = locators["total_price"].text_content().replace("Rs. ", "").strip()

    assert product_data["name"] == product_name, f"Product name mismatch for product {product_id}"
    assert product_data["category"] == product_category, f"Product category mismatch for product {product_id}"
    assert product_data["price"] == product_price, f"Product price mismatch for product {product_id}"
    assert product_quantity == str(quantity), f"Product price mismatch for product {product_id}"
    assert int(product_data["price"]) * int(product_quantity) == int(
        total_price), f"Total price mismatch for product {product_id}"
