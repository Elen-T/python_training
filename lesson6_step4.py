from selenium import webdriver
import time
import math
try:
    link = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Firefox()
    browser.get(link)
    link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
#try:
    #link = "http://suninjuly.github.io/simple_form_find_task.html"
    #browser = webdriver.Firefox()
    #browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Firefox()
browser.get(link)
link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()
#try:
#link = "http://suninjuly.github.io/simple_form_find_task.html"
#browser = webdriver.Firefox()
#browser.get(link)
input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
import os
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element= browser.find_element_by_name("file")
element.send_keys(file_path)