from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    #link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    #login_page = page.go_to_login_page() #Сохранив возвращаемое значение в переменную (объект Page), мы можем использовать методы новой страницы в тесте
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()









def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    #link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()




def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(2)
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_login_form()

def test_guest_should_see_registr_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_register_form()

"""page.should_be_login_link() вызываем функцию should_be_login_link у класса MainPage
def should_be_login_link(self):
    assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented" 
    тут вызываем is_element_present и передаем в него параметры (By.CSS_SELECTOR - how, "#login_link"- what)"""