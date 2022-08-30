from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pass1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        pass2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        print(email_input)
        email_input.send_keys(str(email))
        pass1_input.send_keys(str(password))
        pass2_input.send_keys(str(password))
        reg_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        reg_submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "This is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
