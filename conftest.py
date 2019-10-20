import pytest
import json
from fixture.application import Application
import os.path

fixture = None # глобальная переменная для хранения фикстуры между вызовами
target = None

@pytest.fixture
def app(request): # функция инициализации фикстуры
    global fixture
    global target
    browser = request.config.getoption("--browser")  # извлекаем параметр
    if target is None: # если не определен target, то загружаем конфигурацию из файла
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))  #config_file- путь к файлу file встроенная переменная, которая содержит путь к текущему файлу, используем для задания пути открытия файла конфигурации, os.path.abspath - преобразование пути в абсолютный, os.path.dirname - определение директории в кот находится файл, os.path.join - присоединяем к этому пути абс путь до файла target.json
        with open (config_file) as f: # читаем файлы , f  - объект кот указывает на открытый файл
            target = json.load(f)
    if fixture is None or not fixture.is_valid(): # если фикст не определена или не валидная, тогда ее надо создавать
        fixture = Application(browser=browser, base_url=target["baseUrl"]) # создание фикстуры (объект типа Application), здесь передается параметр browser, который задаетс\я в командной строке
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True) # отдельная фикстура для финализации, должна выполняться в самом конце, тк указано свойство autouse=True
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser): # спец хук, добавляет доп параметры которые можно указать при запуске питест из командной строки и впоследствии можем получить значение которое передано в этом параметре,
    parser.addoption("--browser", action="store", default="firefox") # в параметре парсер передается парсер командной строки, у которого есть метод addoption
    parser.addoption("--target", action="store", default="target.json") # хранение конфигурации в формате json