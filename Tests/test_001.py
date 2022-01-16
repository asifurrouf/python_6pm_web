import time
from tests.base_test import BaseTest
import allure

from Pages.home_page import HomePage

@allure.severity(allure.severity_level.NORMAL)
class Test_001(BaseTest):
    def test_001(self, setUp):
        home_page = HomePage(driver=self.driver)
        home_page.open('')
        time.sleep(10)
        # home_page.scroll_down()
        text = home_page.find_copyright_text()
        assert text == "© 2009–2021 6pm.com or its affiliates"
