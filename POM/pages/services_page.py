from POM.lib.helpers import Helpers
from POM.lib.assertions import assert_that
from selenium.webdriver.common.by import By

class ServicePage(Helpers):
    def __init__(self,driver):
        super().__init__(driver)

    service_page_locator = (By.CLASS_NAME,"top-navigation__item-link")

    def click_on_service_page_locator(self):
        self.find_and_click(self.service_page_locator)

    text_header = (By.CLASS_NAME, "breadcrumbs__item")

    def assert_text_header(self):
        actual_text = self.find(self.assert_text_header, get_text=True)
        assert_that(actual_text = "Home,Our Testing Services")


