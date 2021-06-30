#Задание: поиск сокровища с помощью get_attribute
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    option = browser.find_element_by_id("robotCheckbox")
    option.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()