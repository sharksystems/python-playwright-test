from playwright.sync_api import Page, expect
from pages.page import BasePage


class TestCasesPage(BasePage):
    __test__ = False

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__test_cases__title = self.page.locator('h2.title > b')

    def assert_user_is_on_test_cases_page(self) -> None:
        expect(self.page).to_have_url('https://www.automationexercise.com/test_cases')

    def assert_test_cases_title_visible(self) -> None:
        expect(self.__test_cases__title).to_have_text('Test Cases')
