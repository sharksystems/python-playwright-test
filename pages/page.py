from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.__signup_btn = self.page.locator('a[href="/login"]')
        self.__logout_btn = self.page.locator('a[href="/logout"]')
        self.__delete_account_btn = self.page.locator('a[href="/delete_account"]')
        self.__logged_in_as = self.page.locator('a:has(i.fa-user)>b')
        self.__contact_us_btn = self.page.locator('a[href="/contact_us"]')
        self.__test_cases_btn = self.page.locator('a[href="/test_cases"]').first
        self.__products_btn = self.page.locator('a[href="/products"]')
        self.__cart_btn = self.page.locator('a[href="/view_cart"]').first
        self.__subscribe_input = self.page.locator('#susbscribe_email')
        self.__subscribe_submit_btn = self.page.locator('#subscribe')
        self.__subscribe_text = self.page.locator('div.single-widget>h2')
        self.__subscribe_success_msg = self.page.locator('#success-subscribe')
        self.__continue_shopping_btn = self.page.locator('button.btn-success')
        self.__popup_view_cart_btn = self.page.locator('p.text-center>a')

    def click_signup_btn(self) -> None:
        self.__signup_btn.click()

    def click_delete_account_btn(self) -> None:
        self.__delete_account_btn.click()

    def click_logout_btn(self) -> None:
        self.__logout_btn.click()

    def click_contact_us_btn(self) -> None:
        self.__contact_us_btn.click()

    def click_test_cases_btn(self) -> None:
        self.__test_cases_btn.click()

    def click_products_btn(self) -> None:
        self.__products_btn.click()

    def click_cart_btn(self):
        self.__cart_btn.click()

    def enter_subscription_email(self, email):
        self.__subscribe_input.fill(email)

    def click_subscribe_btn(self):
        self.__subscribe_submit_btn.click()

    def click_popup_continue_shopping(self):
        self.__continue_shopping_btn.click()

    def click_popup_view_cart(self):
        self.__popup_view_cart_btn.click()

    def assert_subscription_success_msg_visible(self):
        expect(self.__subscribe_success_msg).to_be_visible()

    def assert_subscription_title(self):
        expect(self.__subscribe_text).to_have_text("Subscription")

    def assert_logged_in_as(self, username):
        expect(self.__logged_in_as).to_have_text(username)
