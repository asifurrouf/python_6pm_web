from Pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators
    def find_copyright_text(self):
        self.wait_element(*self.locator.COPYRIGHT_TEXT)
        text_element = self.driver.find_element(*self.locator.COPYRIGHT_TEXT)
        text = text_element.text
        return text
    def click_on_shoes(self):
        shoes = self.driver.find_element(*self.locator.SHOES)
        shoes.click()
    def find_shoes_text(self):
        self.wait_element(*self.locator.SHOES)
        text_element = self.driver.find_element(*self.locator.SHOES_TEXT)
        text = text_element.text
        return text

    def click_on_clothing(self):
        clothing = self.driver.find_element(*self.locator.CLOTHING)
        clothing.click()

    def find_clothing_text(self):
        self.wait_element(*self.locator.CLOTHING_TEXT)
        text_element = self.driver.find_element(*self.locator.CLOTHING_TEXT)
        text = text_element.text
        return text

    def click_on_bags(self):
        bags = self.driver.find_element(*self.locator.BAGS)
        bags.click()

    def find_bags_text(self):
        self.wait_element(*self.locator.BAGS_TEXT)
        text_element = self.driver.find_element(*self.locator.BAGS_TEXT)
        text = text_element.text
        return text

    def click_on_accessories(self):
        accessories = self.driver.find_element(*self.locator.ACCESSORIES)
        accessories.click()

    def find_accessories_text(self):
        self.wait_element(*self.locator.ACCESSORIES_TEXT)
        text_element = self.driver.find_element(*self.locator.ACCESSORIES_TEXT)
        text = text_element.text
        return text

    def click_on_womens(self):
        womens = self.driver.find_element(*self.locator.WOMENS)
        womens.click()

    def find_womens_text(self):
        self.wait_element(*self.locator.WOMENS_TEXT)
        text_element = self.driver.find_element(*self.locator.WOMENS_TEXT)
        text = text_element.text
        return text

    def click_on_mens(self):
        mens = self.driver.find_element(*self.locator.MENS)
        mens.click()

    def find_mens_text(self):
        self.wait_element(*self.locator.MENS_TEXT)
        text_element = self.driver.find_element(*self.locator.MENS_TEXT)
        text = text_element.text
        return text

    def click_on_kids(self):
        kids = self.driver.find_element(*self.locator.KIDS)
        kids.click()

    def find_kids_text(self):
        self.wait_element(*self.locator.KIDS_TEXT)
        text_element = self.driver.find_element(*self.locator.KIDS_TEXT)
        text = text_element.text
        return text

    def click_on_clearance(self):
        clearance = self.driver.find_element(*self.locator.CLEARANCE)
        clearance.click()

    def find_clearance_text(self):
        self.wait_element(*self.locator.CLEARANCE_TEXT)
        text_element = self.driver.find_element(*self.locator.CLEARANCE_TEXT)
        text = text_element.text
        return text

    def click_on_brands(self):
        brands = self.driver.find_element(*self.locator.BRANDS)
        brands.click()

    def find_brands_text(self):
        self.wait_element(*self.locator.BRANDS_TEXT)
        text_element = self.driver.find_element(*self.locator.BRANDS_TEXT)
        text = text_element.text
        return text

    def click_and_type_on_search_box(self,search_query):
        search_box = self.driver.find_element(*self.locator.SEARCH_BOX)
        search_box.click()
        search_box.send_keys(search_query)
        submit_btn = self.driver.find_element(*self.locator.SUBMIT_BTN)
        submit_btn.click()

    def find_search_box_text(self):
        self.wait_element(*self.locator.SEARCH_RESULT_TEXT)
        text_element = self.driver.find_element(*self.locator.SEARCH_RESULT_TEXT)
        text = text_element.text
        return text


    def click_on_shop_steve_madden(self):
        shop_stMadden = self.driver.find_element(*self.locator.SHOP_STEVE_MADDEN)
        shop_stMadden.click()

    def find_shop_steve_madden_text(self):
        self.wait_element(*self.locator.SHOP_STEVE_MADDEN_TEXT)
        text_element = self.driver.find_element(*self.locator.SHOP_STEVE_MADDEN_TEXT)
        text = text_element.text
        return text

    def click_on_shop_bebe(self):
        shop_Bebe = self.driver.find_element(*self.locator.SHOP_BEBE)
        shop_Bebe.click()

    def find_shop_bebe_text(self):
        self.wait_element(*self.locator.SHOP_BEBE_TEXT)
        text_element = self.driver.find_element(*self.locator.SHOP_BEBE_TEXT)
        text = text_element.text
        return text

    def click_on_shop_Koolaburra_by_ugg(self):
        shop_Koolaburra = self.driver.find_element(*self.locator.SHOP_KOOLABURRA_BY_UGG)
        shop_Koolaburra.click()

    def find_shop_Koolaburra_by_ugg_text(self):
        self.wait_element(*self.locator.SHOP_KOOLABURRA_BY_UGG_TEXT)
        text_element = self.driver.find_element(*self.locator.SHOP_KOOLABURRA_BY_UGG_TEXT)
        text = text_element.text
        return text

    def click_on_shop_crocs(self):
        shop_crocs = self.driver.find_element(*self.locator.SHOP_CROCS)
        shop_crocs.click()

    def find_shop_crocs_text(self):
        self.wait_element(*self.locator.SHOP_CROCS_TEXT)
        text_element = self.driver.find_element(*self.locator.SHOP_CROCS_TEXT)
        text = text_element.text
        return text

    def click_on_shop_sandals_now(self):
        shop_sandals = self.driver.find_element(*self.locator.SHOP_SANDALS_NOW)
        shop_sandals.click()

    def find_shop_sandals_now_text(self):
        self.wait_element(*self.locator.SHOP_SANDALS_NOW_TEXT)
        text_element = self.driver.find_element(*self.locator.SHOP_SANDALS_NOW_TEXT)
        text = text_element.text
        return text

    def click_on_shop_sneakers_now(self):
        shop_sneakers = self.driver.find_element(*self.locator.SHOP_SNEAKERS_NOW)
        shop_sneakers.click()

    def find_shop_sneakers_now_text(self):
        self.wait_element(*self.locator.SHOP_SANDALS_NOW_TEXT)
        text_element = self.driver.find_element(*self.locator.SHOP_SANDALS_NOW_TEXT)
        text = text_element.text
        return text

    def click_on_shop_now(self):
        shop_now = self.driver.find_element(*self.locator.SHOP_NOW)
        shop_now.click()

    def find_shop_now_text(self):
        self.wait_element(*self.locator.SHOP_NOW_TEXT)
        text_element = self.driver.find_element(*self.locator.SHOP_NOW_TEXT)
        text = text_element.text
        return text


    def click_on_forgot_password(self):
        forgot_password = self.driver.find_element(*self.locator.FORGOT_PASSWORD)
        forgot_password.click()

    def find_forgot_password_text(self):
        self.wait_element(*self.locator.FORGOT_PASSWORD_TEXT)
        text_element = self.driver.find_element(*self.locator.FORGOT_PASSWORD_TEXT)
        text = text_element.text
        return text

    def click_on_shipping_rates(self):
        shipping_rates = self.driver.find_element(*self.locator.SHIPPING_RATES)
        shipping_rates.click()

    def find_shipping_rates_text(self):
        self.wait_element(*self.locator.SHIPPING_RATES_TEXT)
        text_element = self.driver.find_element(*self.locator.SHIPPING_RATES_TEXT)
        text = text_element.text
        return text

    def click_on_return_policy(self):
        return_policy = self.driver.find_element(*self.locator.RETURN_POLICY)
        return_policy.click()

    def find_return_policy_text(self):
        self.wait_element(*self.locator.RETURN_POLICY_TEXT)
        text_element = self.driver.find_element(*self.locator.RETURN_POLICY_TEXT)
        text = text_element.text
        return text
