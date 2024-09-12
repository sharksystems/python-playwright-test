from playwright.sync_api import Page, expect
from pages.page import BasePage


class AccountMessagePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')
        self.__account_creation_success_msg = self.page.locator('h2[data-qa="account-created"]')
        self.__account_deleted_msg = self.page.locator('h2[data-qa="account-deleted"]')

    def assert_account_created_msg_displayed(self) -> None:
        expect(self.__account_creation_success_msg).to_be_visible()

    def assert_account_deleted_msg_displayed(self) -> None:
        expect(self.__account_deleted_msg).to_be_visible()

    def click_continue_btn(self) -> None:
        self.__continue_btn.click()
