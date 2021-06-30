#Задание: принимаем alert
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()