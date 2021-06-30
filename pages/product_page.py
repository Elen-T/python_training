from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProductPage(BasePage):

    def add_basket(self):
        self.browser.find_element(*ProductPageLocators.add_basket).click()

    def solve_quiz_and_get_code(self):  # метод в тесте для получения проверочного кода
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            time.sleep(2)
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    # ТУТ ДОБАВИТЬ АССЕРТЫ
    #для ассерта взять цену с главной страницы price_1 = browser.find_element_by_class_name('price_color').text.
    #Беру цену товара следующим образом
    #ITEM_PRICE = (By.CSS_SELECTOR, "div .price_color")
    #item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text


     #def should_be_login_link(self):
     #   self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
