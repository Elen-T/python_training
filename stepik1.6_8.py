from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Firefox()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла




import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    инпут = browser.find_element_by_id("input_value").сенд кейс(y)
    option1 = browser.find_element_by_css_selector("[value='I'm the robot']")
     option1.click()
    option2 = browser.find_element_by_css_selector("[value='People rule]")
option2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла













