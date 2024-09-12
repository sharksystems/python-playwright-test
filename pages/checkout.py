from playwright.sync_api import Page, expect

from pages.page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__address_details_title = self.page.locator('.step-one h2').first
        self.__review_order_title = self.page.locator('.checkout-information ~ .step-one h2')
        self.__comment_input = self.page.locator('.form-control')
        self.__checkout_submit_btn = self.page.locator('a.check_out')

    def assert_address_details_title_visible(self) -> None:
        expect(self.__address_details_title).to_have_text('Address Details')

    def assert_review_order_title_visible(self) -> None:
        expect(self.__review_order_title).to_have_text('Review Your Order')

    def enter_comment(self, comment):
        self.__comment_input.fill(comment)

    def click_to_payment_btn(self):
        self.__checkout_submit_btn.click()
