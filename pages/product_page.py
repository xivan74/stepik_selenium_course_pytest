from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def compare_product_and_basket_names(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip() == self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text.strip(), \
                "Names are not equal"

    def compare_product_and_basket_prices(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip() == self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE).text.strip(), \
                "Prices are not equal"

    def press_add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def success_text_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.CART_PRODUCT_NAME), "Cart message not found"

    def success_text_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.CART_PRODUCT_NAME), "Cart message not found"



