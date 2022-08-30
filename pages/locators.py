from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages :first-child .alertinner strong")
    ITEM_NAME = (By.CSS_SELECTOR, "ul.breadcrumb li.active")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages :last-child.alert-info .alertinner p strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "div#content_inner > p > a")
