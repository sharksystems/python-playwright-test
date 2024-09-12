from playwright.sync_api import Page
from helpers.product_helpers import verify_product_details
from pages.page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__name = self.page.locator("div.product-information>h2")
        self.__price = self.page.locator("div.product-information>span>span")
        self.__product_category = self.page.locator('div.product-information>p').first
        self.__quantity_input = self.page.locator('#quantity')
        self.__add_to_cart = self.page.locator('.product-information button')

    def verify_product_on_page(self, product_id: str):
        locators = {
            "name": self.__name,
            "price": self.__price,
            "category": self.__product_category,
        }
        verify_product_details(product_id, locators)

    def set_product_quantity(self, quantity):
        self.__quantity_input.fill(quantity)

    def click_add_to_cart(self):
        self.__add_to_cart.click()
