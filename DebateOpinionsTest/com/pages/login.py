from DebateOpinionsTest.com.locators.locators import Locators

class Login:

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_form(self):
        self.driver.find_element_by_link_text(Locators.sign_in_nav_linkText).click()

    def input_username(self, email):
        self.driver.find_element_by_id(Locators.email_textbox_id).send_keys(email)

    def input_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element_by_id(Locators.sign_in_button_id).click()

    def get_sign_in_error_message(self):
        return self.driver.find_element_by_css_selector(Locators.invalid_sign_in_message_css).text
