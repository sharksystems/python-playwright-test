from playwright.sync_api import Page, expect

from pages.page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__search_input = self.page.locator('input#search_product')
        self.__search_submit = self.page.locator('button#submit_search')
        self.__search_result_name = self.page.locator('div.single-products p').first

    def click_view_product_by_id(self, product_id: str):
        self.page.locator(f"a[href='/product_details/{product_id}']").click()

    def click_add_to_cart_by_id(self, product_id: str):
        overlay_add_to_cart = self.page.locator(f".product-overlay a[data-product-id='{product_id}']")
        add_to_cart = self.page.locator(f".productinfo >a[data-product-id='{product_id}']")

        add_to_cart.hover()
        overlay_add_to_cart.click()

    def enter_search(self, value):
        self.__search_input.fill(value)

    def click_search_btn(self):
        self.__search_submit.click()

    def search_product_and_verify(self, name):
        self.enter_search(name)
        self.click_search_btn()
        expect(self.__search_result_name).to_have_text(name)
