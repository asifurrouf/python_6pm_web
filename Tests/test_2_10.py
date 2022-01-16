from tests.base_test import BaseTest
import allure
from Pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_2_10(BaseTest):
    def test_2_10(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        self.driver.implicitly_wait(15)
        home_page.click_on_accessories()
        self.driver.implicitly_wait(15)
        text = home_page.find_accessories_text()
        assert text == "Accessories"

