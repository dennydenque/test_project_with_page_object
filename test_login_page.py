from .pages.login_page import LoginPage


def test_guest_can_login_and_register(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

