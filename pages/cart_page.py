from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_text_that_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.BASKET_IS_EMPTY_TEXT), "'Basket is empty' text not found"

