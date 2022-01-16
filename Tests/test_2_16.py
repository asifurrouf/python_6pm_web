from tests.base_test import BaseTest
import allure
from Pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_2_16(BaseTest):
    def test_2_16(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        self.driver.implicitly_wait(15)
        home_page.click_on_shop_sneakers_now()
        self.driver.implicitly_wait(15)
        text = home_page.find_shop_sneakers_now_text()
        assert text == "Sneakers & Athletic Shoes"

