from selenium import webdriver
import unittest
from DebateOpinionsTest.com.pages.navigation import Navigation
from DebateOpinionsTest.com.pages.base_page import BasePage


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/hollyliulka/PycharmProjects/DebateOpinionsTest/com/drivers/chromedriver")
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()
        self.driver.get("https://www.debate.org/opinions/")
        self.nav = Navigation(self.driver)
        self.base = BasePage(self.driver)

    # test corresponds with Test Case ID 1
    # verify page header changes when a new category is selected
    def test_art_link_filters_art_opinions(self):

        self.nav.select_arts_side_nav()
        actual_title = self.base.get_page_header()
        print(actual_title)
        assert "Arts Opinions" in actual_title

    # test corresponds with Test Case ID 2
    # verify page header changes when a new category is selected
    def test_entertainment_link_filters_entertainment_opinions(self):

        self.nav.select_entertainment_side_nav()
        actual_title = self.base.get_page_header()
        print(actual_title)
        assert "Entertainment Opinions" in actual_title

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
