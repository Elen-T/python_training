import pytest
from fixture.application import Application

fixture = None # глобальная переменная для хранения фикстуры между вызовами


@pytest.fixture
def app(request): # функция инициализации фикстуры
    global fixture
    if fixture is None:
        fixture = Application() # создание фикстуры (объект типа Application)
        # проверка предусловия
        fixture.session.ensure_login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True) # отдельная фикстура для финализации, должна выполняться в самом конце, тк указано свойство autouse=True
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
