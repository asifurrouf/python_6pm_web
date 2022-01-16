from tests.base_test import BaseTest
import allure
from Pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_2_11(BaseTest):
    def test_2_11(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        self.driver.implicitly_wait(15)
        home_page.click_on_shop_steve_madden()
        self.driver.implicitly_wait(15)
        text = home_page.find_shop_steve_madden_text()
        assert text == "Steve Madden"

