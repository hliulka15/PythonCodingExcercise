from com.locators.locators import Locators

class Navigation:

    def __init__(self, driver):
        self.driver = driver

    def select_arts_side_nav(self):

        self.driver.find_element_by_link_text(Locators.sidebar_arts_linkText).click()

    def select_cars_side_nav(self):
        self.driver.find_element_by_link_text(Locators.sidebar_cars_linkText).click()

    def select_economics_side_nav(self):
        self.driver.find_element_by_link_text(Locators.sidebar_economics_linkText).click()

    def select_education_side_nav(self):
        self.driver.find_element_by_link_text(Locators.sidebar_education_linkText).click()

    def select_entertainment_side_nav(self):
        self.driver.find_element_by_link_text(Locators.sidebar_entertainment_linkText).click()

