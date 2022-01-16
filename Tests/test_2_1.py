import time
from tests.base_test import BaseTest
import allure
from Pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_002(BaseTest):
    def test_002(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        self.driver.implicitly_wait(15)
        home_page.click_on_shoes()
        self.driver.implicitly_wait(15)
        text = home_page.find_shoes_text()
        assert text == "Shoes"

