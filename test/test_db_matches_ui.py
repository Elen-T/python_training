# тест для проверки соответствия списка групп выгруженного из БД и из приложения
from model.group import Group
from timeit import timeit # для измерения времени


def test_group_list(app, db):  # передаем два параметра app - для получения доступа к приложению, db - фикстура для получения доступа к бд
    print(timeit(lambda: app.group.get_group_list(), number=1))  # измеряем время выполнения lambda(функции загрузки чз приложение), вызов 1 раз number=1
    def clean(group):  # удляем лишние пробелы в начале и конце, после применения этой ф-ии объекты в обоих случаях д выглядеть одинаково
         return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))  # список загруженный через бд, применяем к списку функцию clean
    #assert False #False - чтобы тест упал и получитьвывод на консоль # sorted(ui_list, key=Group.id_or_max) == sorted(db_list,key=Group.id_or_max)  # проверка отсортированных списков



"""def test_group_list(app, db):  # передаем два параметра app - для получения доступа к приложению, db - фикстура для получения доступа к бд
    ui_list = app.group.get_group_list()  # сравниваем результаты, список загруженный через приложение
    def clean(group):  # удляем лишние пробелы в начале и конце, после применения этой ф-ии объекты в обоих случаях д выглядеть одинаково
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())  # список загруженный через бд, применяем к списку функцию clean
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list,key=Group.id_or_max)  # проверка отсортированных списков"""
