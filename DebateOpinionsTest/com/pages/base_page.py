class BasePage():

    def __init__(self, driver):
        self.driver = driver

        self.page_header_css = "#pg-head > h1"

    def get_page_header(self):
        return self.driver.find_element_by_css_selector(self.page_header_css).text
