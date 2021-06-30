#Задание: работа с выпадающим списком
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    s = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    str1=str(s)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str1)

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()