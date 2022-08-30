from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Some items in basket"

    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING), "Can't find 'basket empty' text"

