from tests.base_test import BaseTest
import allure
from Pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_2_9(BaseTest):
    def test_2_9(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        self.driver.implicitly_wait(15)
        search_query = 'mobile phone'
        home_page.click_and_type_on_search_box(search_query)
        self.driver.implicitly_wait(15)
        text = home_page.find_search_box_text()
        assert text == search_query.title()

