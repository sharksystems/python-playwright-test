from playwright.sync_api import Page

from helpers.product_helpers import verify_cart_product_details
from pages.page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__popup_signup_btn = self.page.locator('.modal-body a')
        self.__checkout_btn = self.page.locator('a.check_out')

    def click_popup_signup_btn(self):
        self.__popup_signup_btn.click()

    def click_checkout_btn(self):
        self.__checkout_btn.click()

    def verify_product_in_cart(self, product_id: str, product_index, product_quantity: int):
        locators = {
            "name": self.page.locator(f"#product-{product_index}>td.cart_description>h4>a"),
            "category": self.page.locator(f"#product-{product_index}>td.cart_description p"),
            "price": self.page.locator(f"#product-{product_index}>td.cart_price>p"),
            "total_price": self.page.locator(f"#product-{product_index}>td.cart_total>p"),
            "quantity": self.page.locator(f"#product-{product_index}>td.cart_quantity button")
        }
        verify_cart_product_details(locators, product_id, product_quantity)
