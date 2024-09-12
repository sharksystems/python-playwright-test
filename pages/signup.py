from playwright.sync_api import Page, expect
from pages.page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__new_user_signup_text = self.page.locator("//h2[text()='New User Signup!']")
        self.__signup_name_field = self.page.locator("input[data-qa='signup-name']")
        self.__signup_email_field = self.page.locator("input[data-qa='signup-email']")
        self.__signup_submit_btn = self.page.locator("button[data-qa='signup-button']")
        self.__login_email_field = self.page.locator("input[data-qa='login-email']")
        self.__login_password_field = self.page.locator("input[data-qa='login-password']")
        self.__login_submit_btn = self.page.locator("button[data-qa='login-button']")
        self.__error_msg = self.page.locator("p[style='color: red;']")

    def enter_signup_name(self, name) -> None:
        self.__signup_name_field.fill(name)

    def enter_signup_email(self, email) -> None:
        self.__signup_email_field.fill(email)

    def click_signup_submit_btn(self) -> None:
        self.__signup_submit_btn.click()

    def enter_login_email(self, email) -> None:
        self.__login_email_field.fill(email)

    def enter_login_password(self, password) -> None:
        self.__login_password_field.fill(password)

    def click_login_submit_btn(self) -> None:
        self.__login_submit_btn.click()

    def assert_user_is_on_signup_page(self) -> None:
        expect(self.page).to_have_url('https://www.automationexercise.com/login')

    def assert_email_password_incorrect_msg_visible(self) -> None:
        expect(self.__error_msg).to_have_text('Your email or password is incorrect!')

    def assert_email_taken_msg_visible(self) -> None:
        expect(self.__error_msg).to_have_text('Email Address already exist!')
