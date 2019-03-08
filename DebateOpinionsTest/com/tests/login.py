from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
from DebateOpinionsTest.com.pages.login import Login


class LoginTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("/Users/hollyliulka/PycharmProjects/DebateOpinionsTest/com/drivers/chromedriver")
        self.driver.set_page_load_timeout(30)
        self.driver.get("https://www.debate.org/opinions/")
        self.login = Login(self.driver)

    def test_invalid_login_captcha(self):
        self.login.go_to_login_form()
        self.login.input_username("hollystests@gmail.com")
        self.login.input_password("Testpass1")

        # login ended up not working because of the captcha. So Instead,
        # verified captcha cannot be clicked and logging in would fail.
        # originally this was intended to be in the login page. However, since
        # it was destined to fail I decided to turn it into a bonus test case

        try:
            self.driver.find_element_by_id("recaptcha-anchor").click()
        except NoSuchElementException: print("cannot use captcha")

        self.login.click_sign_in_button()

        captcha_error_message = self.login.get_sign_in_error_message()

        assert "Please, complete reCaptcha." in captcha_error_message

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
