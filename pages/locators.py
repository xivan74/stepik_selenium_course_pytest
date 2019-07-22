from selenium.webdriver.common.by import By

class BasePageLocators(object):
    CART_LINK = (By.XPATH, '//span[@class="btn-group"]/a[contains(@href, "/basket/")]')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    REGISTER_FORM_EMAIL = (By.XPATH, '//form[@id="register_form"]//input[@name="registration-email"]')
    REGISTER_FORM_PASSWORD = (By.XPATH, '//form[@id="register_form"]//input[@name="registration-password1"]')
    REGISTER_FORM_PASSWORD_CONFIRM = (By.XPATH, '//form[@id="register_form"]//input[@name="registration-password2"]')
    REGISTER_FORM_BUTTON = (By.XPATH, '//form[@id="register_form"]//button[@name="registration_submit"]')

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    PROMO_URL = "?promo=newYear"
    BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]/p[@class="price_color"]')
    CART_PRODUCT_NAME = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    CART_PRODUCT_PRICE = (By.XPATH, '//div[@id="messages"]/div[3]/div/p[1]/strong')
    CART_LINK = (By.XPATH, '//span[@class="btn-group"]/a[contains(@href, "/basket/")]')

class CartPageLocators(object):
    BASKET_ITEMS = (By.XPATH, '//div[@class="basket-items"]')
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//div[@id="content_inner"]/p[contains(text(), "Your basket is empty")]')
    

