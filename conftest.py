import pytest
import json
from fixture.application import Application
import os.path
import importlib
import jsonpickle

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

# Ещё один способ параметризации тестов: динамическая генерация тестов
# НЕ использовать....
def pytest_generate_tests(metafunc): #matafunc - спец объект для получения инфы о тестовой функции
    for fixture in metafunc.fixturenames: #проход по всем параметрам, но интересуют те кот начинаются с data_
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:]) # как только встретилась такая фикстура, загружаем тест данные из модуля fixture, 5: - удаление 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])#используем загруженные тестовые данные чтобы параметризовать тест функцию, параметры подставляются в качестве значения фикстуры, ids - строковое представление
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[ 5:])  # как только встретилась такая фикстура, загружаем тест данные из json файла, 5: - удаление 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])  # используем загруженные тестовые данные чтобы параметризовать тест функцию, параметры подставляются в качестве значения фикстуры, ids - строковое представление


def load_from_module (module): #загрузка данных из модуля\
    return importlib.import_module("data.%s" % module).testdata # после того как моодуль импортирован нужно взять из него testdata


def load_from_json (file): #загрузка данных из
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f: # строим путь к файлу, берем путь к текущему файлу, получаем директорию в кот он находится
        return jsonpickle.decode(f.read()) # после открытия читаем из него данные и перекодируем с помощью jsonpickle в вид набора объектов питон