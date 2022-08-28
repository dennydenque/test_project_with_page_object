from .pages.product_page import ProductPage
from .pages.product_page import ProductPageLocators

import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_add_basket_message()
    page.should_be_message_price_equal_basket()

