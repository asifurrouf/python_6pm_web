from tests.base_test import BaseTest
import allure
from Pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_2_3(BaseTest):
    def test_2_3(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        self.driver.implicitly_wait(15)
        home_page.click_on_bags()
        self.driver.implicitly_wait(15)
        text = home_page.find_bags_text()
        assert text == "Bags"

