from POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By

class HomePageFunctionality(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    get_a_demo = (By.CLASS_NAME, "cta-button__button.button-cta--get-a-demo")

    def click_on_get_a_demo(self):
        self.find_and_click(self.get_a_demo,self.driver)

    become_a_tester = (By.CSS_SELECTOR, '[class="cta-button__button.button-cta--become-a-tester"]')
    def click_on_a_become_a_tester(self):
        self.find_and_click(self.become_a_tester)
