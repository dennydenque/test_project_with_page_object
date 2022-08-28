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
        assert item_name in message_text, "Add to basket message is not presented"

    def should_be_message_price_equal_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        basket_text = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert price in basket_text, "Incorrect sum in basket"