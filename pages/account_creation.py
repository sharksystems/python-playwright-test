from playwright.sync_api import Page, expect
from pages.page import BasePage


class AccountCreationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__enter_account_information_title = self.page.locator('h2>b').first
        self.__name_input = self.page.locator('#name')
        self.__email_input = self.page.locator('#email')
        self.__password_input = self.page.locator('#password')
        self.__day_select_field = self.page.locator('#days')
        self.__month_select_field = self.page.locator('#months')
        self.__year_select_field = self.page.locator('#years')
        self.__newsletter_checkbox = self.page.locator('#newsletter')
        self.__offers_checkbox = self.page.locator('#optin')
        self.__first_name_input = self.page.locator('#first_name')
        self.__last_name_input = self.page.locator('#last_name')
        self.__company_input = self.page.locator('#company')
        self.__address_input = self.page.locator('#address1')
        self.__address2_input = self.page.locator('#address2')
        self.__country_select_field = self.page.locator('#country')
        self.__state_input = self.page.locator('#state')
        self.__city_input = self.page.locator('#city')
        self.__zipcode_input = self.page.locator('#zipcode')
        self.__mobile_number_input = self.page.locator('#mobile_number')
        self.__create_account_btn = self.page.locator('button[data-qa="create-account"]')

    def choose_title(self, choose_mr=True) -> None:
        if choose_mr:
            self.page.check("#id_gender1")
        else:
            self.page.check("#id_gender2")

    def enter_name(self, name) -> None:
        self.__name_input.fill(name)

    def enter_email(self, email) -> None:
        self.__email_input.fill(email)

    def enter_password(self, password) -> None:
        self.__password_input.fill(password)

    def select_date_day(self, day) -> None:
        self.__day_select_field.select_option(day)

    def select_date_month(self, month) -> None:
        self.__month_select_field.select_option(month)

    def select_date_year(self, year) -> None:
        self.__year_select_field.select_option(year)

    def click_newsletter_checkbox(self) -> None:
        self.__newsletter_checkbox.click()

    def click_offers_checkbox(self) -> None:
        self.__offers_checkbox.click()

    def enter_first_name(self, first_name) -> None:
        self.__first_name_input.fill(first_name)

    def enter_last_name(self, last_name) -> None:
        self.__last_name_input.fill(last_name)

    def enter_company(self, company) -> None:
        self.__company_input.fill(company)

    def enter_address(self, address) -> None:
        self.__address_input.fill(address)

    def enter_address2(self, address2) -> None:
        self.__address2_input.fill(address2)

    def select_country(self, country) -> None:
        self.__country_select_field.select_option(country)

    def enter_state(self, state) -> None:
        self.__state_input.fill(state)

    def enter_city(self, city) -> None:
        self.__city_input.fill(city)

    def enter_zipcode(self, zipcode) -> None:
        self.__zipcode_input.fill(zipcode)

    def enter_mobile_number(self, mobile_number) -> None:
        self.__mobile_number_input.fill(mobile_number)

    def click_create_account_submit_btn(self) -> None:
        self.__create_account_btn.click()

    def assert_enter_details_title_displayed(self) -> None:
        expect(self.__enter_account_information_title).to_have_text('Enter Account Information')
