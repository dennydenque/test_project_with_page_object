import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.skip(reason="bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_add_basket_message()
    page.should_be_message_price_equal_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="bug")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappear_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_empty_text()


@pytest.mark.reg
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(str(time.time()) + "@fakemail.org", 'POI147852')
        login_page.should_be_authorized_user()
        return self.setup

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        browser.get(link)
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket(is_guest=False)
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        browser.get(link)
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket(is_guest=False)
        page.should_be_add_basket_message()
        page.should_be_message_price_equal_basket()
