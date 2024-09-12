from playwright.sync_api import Page, expect

from pages.page import BasePage


class PaymentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__name_on_card_input = self.page.locator("input[data-qa='name-on-card']")
        self.__card_number_input = self.page.locator("input[data-qa='card-number']")
        self.__cvc_input = self.page.locator("input[data-qa='cvc']")
        self.__expiration_month_input = self.page.locator("input[data-qa='expiry-month']")
        self.__expiration_year_input = self.page.locator("input[data-qa='expiry-year']")
        self.__payment_submit_btn = self.page.locator("button[data-qa='pay-button']")
        self.__payment_successful_msg = self.page.locator("h2[data-qa='order-placed']")

    def enter_name_on_card(self, name):
        self.__name_on_card_input.fill(name)

    def enter_card_number(self, number):
        self.__card_number_input.fill(number)

    def enter_cvc(self, cvc):
        self.__cvc_input.fill(cvc)

    def enter_expiration_month(self, month):
        self.__expiration_month_input.fill(month)

    def enter_expiration_year(self, year):
        self.__expiration_year_input.fill(year)

    def click_payment_submit_btn(self):
        self.__payment_submit_btn.click()

    def assert_payment_successful_msg_visible(self) -> None:
        expect(self.__payment_successful_msg).to_have_text('Order Placed!')
