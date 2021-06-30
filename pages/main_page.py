from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)#Затем в методе, который осуществляет переход к странице логина,
        # проинициализировать новый объект Page и вернуть его:

        #def should_be_login_link(self):
     #   self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.