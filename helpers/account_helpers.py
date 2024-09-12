from pages.home import HomePage
from pages.signup import SignupPage
from pages.account_creation import AccountCreationPage
from pages.account_message import AccountMessagePage


def create_account(page, user):
    signup_page = SignupPage(page)
    account_creation_page = AccountCreationPage(page)
    account_message_page = AccountMessagePage(page)

    signup_page.enter_signup_name(user.username)
    signup_page.enter_signup_email(user.email)
    signup_page.click_signup_submit_btn()

    account_creation_page.assert_enter_details_title_displayed()
    account_creation_page.choose_title()
    account_creation_page.enter_name(user.username)
    account_creation_page.enter_password(user.password)
    account_creation_page.select_date_day(user.birth_day)
    account_creation_page.select_date_month(user.birth_month)
    account_creation_page.select_date_year(user.birth_year)
    account_creation_page.click_newsletter_checkbox()
    account_creation_page.click_offers_checkbox()
    account_creation_page.enter_first_name(user.first_name)
    account_creation_page.enter_last_name(user.last_name)
    account_creation_page.enter_company(user.company_name)
    account_creation_page.enter_address(user.address)
    account_creation_page.enter_address2(user.address2)
    account_creation_page.select_country(user.country)
    account_creation_page.enter_state(user.state)
    account_creation_page.enter_city(user.city)
    account_creation_page.enter_zipcode(user.zipcode)
    account_creation_page.enter_mobile_number(user.mobile_number)
    account_creation_page.click_newsletter_checkbox()
    account_creation_page.click_offers_checkbox()
    account_creation_page.click_create_account_submit_btn()
    account_message_page.assert_account_created_msg_displayed()
    account_message_page.click_continue_btn()


def delete_account(page):
    home_page = HomePage(page)
    account_message_page = AccountMessagePage(page)

    home_page.click_delete_account_btn()
    account_message_page.assert_account_deleted_msg_displayed()
    account_message_page.click_continue_btn()


def login(page, user):
    home_page = HomePage(page)
    signup_page = SignupPage(page)

    home_page.click_signup_btn()
    signup_page.enter_login_email(user.email)
    signup_page.enter_login_password(user.password)
    signup_page.click_login_submit_btn()
