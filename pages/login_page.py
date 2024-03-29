from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM)
        password_input2.send_keys(password)
        register_form_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        register_form_button.click()
        
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login string not found in page URL"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
