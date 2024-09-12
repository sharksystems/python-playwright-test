import os
from playwright.sync_api import Page, expect
from pages.page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__contact_us_title = self.page.locator('div.col-sm-12 > h2')
        self.__name_input = self.page.locator("input[data-qa='name']")
        self.__email_input = self.page.locator("input[data-qa='email']")
        self.__subject_input = self.page.locator("input[data-qa='subject']")
        self.__message_input = self.page.locator("textarea[data-qa='message']")
        self.__file_upload = self.page.locator("input[type='file']")
        self.__submit_btn = self.page.locator("input[data-qa='submit-button']")
        self.__submitted_successfully_msg = self.page.locator("div.alert-success").first

    def enter_name(self, name) -> None:
        self.__name_input.fill(name)

    def enter_email(self, email) -> None:
        self.__email_input.fill(email)

    def enter_subject(self, subject) -> None:
        self.__subject_input.fill(subject)

    def enter_message(self, message) -> None:
        self.__message_input.fill(message)

    def upload_file(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, '..', 'files', 'contact_us_file.pdf')
        self.__file_upload.set_input_files(file_path)

    def click_submit_btn(self) -> None:
        self.page.wait_for_timeout(1000)
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.__submit_btn.click()

    def assert_contact_us_title_visible(self) -> None:
        expect(self.__contact_us_title).to_have_text('Contact Us')

    def assert_submission_successful_msg_visible(self) -> None:
        expect(self.__submitted_successfully_msg).to_have_text(
            'Success! Your details have been submitted successfully.')
