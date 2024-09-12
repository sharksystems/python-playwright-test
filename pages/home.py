from playwright.sync_api import Page, expect
from pages.page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def assert_user_is_on_homepage(self) -> None:
        expect(self.page).to_have_url('https://www.automationexercise.com/')
