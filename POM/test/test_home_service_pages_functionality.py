import pytest



@pytest.mark.usefixtures('get_driver')
class TestTwoPagesFunctions:

    def test_two_pages_functionality(self):
        self.home_page.click_on_get_a_demo()
        self.home_page.click_on_a_become_a_tester()
        self.services_page.click_on_service_page_locator()
        self.services_page.assert_text_header()

