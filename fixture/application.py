from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, base_url ):
        if  browser=="firefox":
            self.wd = webdriver.Firefox()  # инициализация, запуск браузера, создание объекта webdriver
        elif browser=="chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser) # если нет заданного браузера, то возникает исключение, выполнение кода будет прервано
        self.wd.implicitly_wait(10)
        # инициализация помощников, получает ссылку на объект класса Application
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self): # проверка получения текущего адреса у открытой страницы
        try:
            self.wd.current_url
            return True
        except: # если возникли проблемы при получении то False, фикстура не валидна
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)  # адрес тестируемого приложения в качестве параметра


    def destroy(self): # разрушает фикстуру, останавливает браузер
        self.wd.quit()
