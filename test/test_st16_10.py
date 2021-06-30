from selenium import webdriver
import time
#import unittest
import pytest

#class TestAbs(unittest.TestCase):

def test_st16_10():

    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("1@1.qw")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


def test_st16_100():

        try:
            # link = "http://suninjuly.github.io/registration1.html"
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Firefox()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input.form-control.first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input.form-control.second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_class_name("form-control.third")
            input3.send_keys("1@1.qw")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

#if __name__ == "__main__":
#    unittest.main()
