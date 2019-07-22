from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time
import pytest

@pytest.mark.login
class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        self.page = LoginPage(browser, self.login_link)
        self.page.open() 
        email = str(time.time()) + "@fakemail.org"
        password = "867530900"
        self.browser = browser
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(self.browser, self.product_link)
        self.page.open()
        self.page.success_text_is_not_present()

    def test_user_can_add_product_to_cart(self):
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = ProductPage(self.browser, self.product_link)
        self.page.open()
        self.page.press_add_to_basket_button()
        self.page.solve_quiz_and_get_code()
        self.page.compare_product_and_basket_names()
        self.page.compare_product_and_basket_prices()


def test_guest_can_add_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, product_link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page.open()                      # открываем страницу
    product_page.press_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.compare_product_and_basket_names()
    product_page.compare_product_and_basket_prices()

def test_guest_should_see_login_link_on_product_page(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()    

def test_guest_cant_see_success_message(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.success_text_is_not_present()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_text_that_empty_cart()


