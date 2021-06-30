from selenium.webdriver.common.by import By


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link") # теперь каждый селектор — это пара: как искать и что искать
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    #LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6 login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    add_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
