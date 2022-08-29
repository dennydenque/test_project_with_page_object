import pytest

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_add_basket_message(self):
        message_text = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text.strip("\" ")
        assert item_name == message_text, "Wrong item name in add to basket message"

    def should_be_message_price_equal_basket(self):
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price == price_message, "Wrong price in basket status message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE), \
                "Success message is presented, but should not be"

    def should_be_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE), \
                "Success message should be disappear"

