#Задание: переход на новую вкладку
from selenium import webdriver
import time
import re
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()


    browser.switch_to.window(browser.window_handles[1])

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
    print(text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()