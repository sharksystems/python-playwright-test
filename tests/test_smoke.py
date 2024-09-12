import pytest

from conftest import new_page
from utils.tools import take_screenshot
from data.random_user import RandomUser
from helpers.account_helpers import create_account, delete_account, login
from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.contact_us import ContactUsPage
from pages.home import HomePage
from pages.payment import PaymentPage
from pages.product_detail import ProductDetailPage
from pages.products import ProductsPage
from pages.signup import SignupPage
from pages.account_creation import AccountCreationPage
from pages.account_message import AccountMessagePage
from pages.test_cases import TestCasesPage


class TestSmoke:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.random_user = RandomUser()
        self.invalid_user = RandomUser()
        self.home_page = HomePage(self.page)
        self.signup_page = SignupPage(self.page)
        self.account_creation_page = AccountCreationPage(self.page)
        self.account_message_page = AccountMessagePage(self.page)
        self.contact_us_page = ContactUsPage(self.page)
        self.test_cases_page = TestCasesPage(self.page)
        self.products_page = ProductsPage(self.page)
        self.product_detail_page = ProductDetailPage(self.page)
        self.cart_page = CartPage(self.page)
        self.checkout_page = CheckoutPage(self.page)
        self.payment_page = PaymentPage(self.page)

    def test_signup(self, test_setup):
        self.home_page.click_signup_btn()
        create_account(self.page, self.random_user)
        self.home_page.assert_logged_in_as(self.random_user.username)
        delete_account(self.page)
        self.home_page.assert_user_is_on_homepage()
        take_screenshot(self.page, 'test_signup')

    def test_login(self, test_setup):
        self.home_page.click_signup_btn()
        create_account(self.page, self.random_user)
        self.home_page.click_logout_btn()
        self.home_page.click_signup_btn()
        self.signup_page.enter_login_email(self.random_user.email)
        self.signup_page.enter_login_password(self.random_user.password)
        self.signup_page.click_login_submit_btn()
        self.home_page.assert_logged_in_as(self.random_user.username)
        delete_account(self.page)
        take_screenshot(self.page, 'test_login')

    def test_invalid_login(self, test_setup):
        login(self.page, self.random_user)
        self.signup_page.assert_email_password_incorrect_msg_visible()
        take_screenshot(self.page, 'test_invalid_login')

    def test_logout(self, test_setup):
        self.home_page.click_signup_btn()
        create_account(self.page, self.random_user)
        self.home_page.click_logout_btn()
        self.signup_page.assert_user_is_on_signup_page()
        login(self.page, self.random_user)
        delete_account(self.page)
        take_screenshot(self.page, 'test_logout')

    def test_existing_email_registration(self, test_setup):
        self.home_page.click_signup_btn()
        create_account(self.page, self.random_user)
        self.home_page.click_logout_btn()
        self.signup_page.enter_signup_name(self.random_user.username)
        self.signup_page.enter_signup_email(self.random_user.email)
        self.signup_page.click_signup_submit_btn()
        self.signup_page.assert_email_taken_msg_visible()
        login(self.page, self.random_user)
        delete_account(self.page)
        take_screenshot(self.page, 'test_existing_email_registration')

    def test_contact_form(self, test_setup):
        self.home_page.click_contact_us_btn()
        self.contact_us_page.assert_contact_us_title_visible()
        self.contact_us_page.enter_name(self.random_user.first_name)
        self.contact_us_page.enter_email(self.random_user.email)
        self.contact_us_page.enter_subject(self.random_user.random_subject)
        self.contact_us_page.enter_message(self.random_user.random_message)
        self.contact_us_page.upload_file()
        self.contact_us_page.click_submit_btn()
        self.contact_us_page.assert_submission_successful_msg_visible()
        take_screenshot(self.page, 'test_contact_form')

    def test_cases_page(self, test_setup):
        self.home_page.click_test_cases_btn()
        self.test_cases_page.assert_user_is_on_test_cases_page()
        self.test_cases_page.assert_test_cases_title_visible()
        take_screenshot(self.page, 'test_cases_page')

    def test_verify_all_products_and_details(self, test_setup):
        self.home_page.click_products_btn()
        self.products_page.click_view_product_by_id("1")
        self.product_detail_page.verify_product_on_page("1")
        take_screenshot(self.page, 'test_verify_all_products_and_details')

    def test_product_search(self, test_setup):
        self.home_page.click_products_btn()
        self.products_page.search_product_and_verify("Blue Top")
        take_screenshot(self.page, 'test_product_search')

    def test_subscription_homepage(self, test_setup):
        self.home_page.assert_subscription_title()
        self.home_page.enter_subscription_email(self.random_user.email)
        self.home_page.click_subscribe_btn()
        self.home_page.assert_subscription_success_msg_visible()
        take_screenshot(self.page, 'test_subscription_homepage')

    def test_subscription_cart(self, test_setup):
        self.home_page.click_cart_btn()
        self.cart_page.assert_subscription_title()
        self.cart_page.enter_subscription_email(self.random_user.email)
        self.cart_page.click_subscribe_btn()
        self.cart_page.assert_subscription_success_msg_visible()
        take_screenshot(self.page, 'test_subscription_cart')

    def test_adding_to_cart(self, test_setup):
        self.home_page.click_products_btn()
        self.products_page.click_add_to_cart_by_id("1")
        self.products_page.click_popup_continue_shopping()
        self.products_page.click_add_to_cart_by_id("2")
        self.products_page.click_popup_view_cart()
        self.cart_page.verify_product_in_cart("1", 1, 1)
        self.cart_page.verify_product_in_cart("2", 2, 1)
        take_screenshot(self.page, 'test_adding_to_cart')

    def test_product_quantity(self, test_setup):
        quantity = 4

        self.home_page.click_products_btn()
        self.products_page.click_view_product_by_id("1")
        self.product_detail_page.set_product_quantity(str(quantity))
        self.product_detail_page.click_add_to_cart()
        self.product_detail_page.click_popup_view_cart()
        self.cart_page.verify_product_in_cart("1", 1, quantity)
        take_screenshot(self.page, 'test_product_quantity')

    def test_register_while_checkout(self, test_setup):
        self.home_page.click_products_btn()
        self.products_page.click_add_to_cart_by_id("1")
        self.products_page.click_popup_view_cart()
        self.cart_page.click_checkout_btn()
        self.cart_page.click_popup_signup_btn()
        create_account(self.page, self.random_user)
        self.home_page.click_cart_btn()
        self.cart_page.click_checkout_btn()
        self.checkout_page.assert_address_details_title_visible()
        self.checkout_page.assert_review_order_title_visible()
        self.checkout_page.enter_comment(self.random_user.random_message)
        self.checkout_page.click_to_payment_btn()
        self.payment_page.enter_name_on_card(self.random_user.card_name)
        self.payment_page.enter_card_number(self.random_user.card_number)
        self.payment_page.enter_cvc(self.random_user.card_cvc)
        self.payment_page.enter_expiration_month(self.random_user.expiration_month)
        self.payment_page.enter_expiration_year(self.random_user.expiration_year)
        self.payment_page.click_payment_submit_btn()
        self.payment_page.assert_payment_successful_msg_visible()
        delete_account(self.page)
        take_screenshot(self.page, 'test_register_while_checkout')

    def test_register_before_checkout(self, test_setup):
        self.home_page.click_signup_btn()
        create_account(self.page, self.random_user)
        self.home_page.click_products_btn()
        self.products_page.click_add_to_cart_by_id("1")
        self.products_page.click_popup_view_cart()
        self.cart_page.click_checkout_btn()
        self.checkout_page.assert_address_details_title_visible()
        self.checkout_page.assert_review_order_title_visible()
        self.checkout_page.enter_comment(self.random_user.random_message)
        self.checkout_page.click_to_payment_btn()
        self.payment_page.enter_name_on_card(self.random_user.card_name)
        self.payment_page.enter_card_number(self.random_user.card_number)
        self.payment_page.enter_cvc(self.random_user.card_cvc)
        self.payment_page.enter_expiration_month(self.random_user.expiration_month)
        self.payment_page.enter_expiration_year(self.random_user.expiration_year)
        self.payment_page.click_payment_submit_btn()
        self.payment_page.assert_payment_successful_msg_visible()
        delete_account(self.page)
        take_screenshot(self.page, 'test_register_before_checkout')
