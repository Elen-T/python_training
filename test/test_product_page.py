# https://stepik.org/lesson/201964/step/2?unit=176022
#https://stepik.org/lesson/201964/step/2?thread=solutions&unit=176022 - тут решения

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
import time

def  test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    #page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    # login_page = page.go_to_login_page() #Сохранив возвращаемое значение в переменную (объект Page), мы можем использовать методы новой страницы в тесте
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_basket()
    product_page.solve_quiz_and_get_code()

