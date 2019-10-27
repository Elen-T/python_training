# тест для проверки соответствия списка групп выгруженного из БД и из приложения
from model.group import Group


def test_group_list(app, db):  # передаем два параметра app - для получения доступа к приложению, db - фикстура для получения доступа к бд
    ui_list = app.group.get_group_list()  # сравниваем результаты, список загруженный через приложение
    def clean(group):  # удляем лишние пробелы в начале и конце, после применения этой ф-ии объекты в обоих случаях д выглядеть одинаково
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())  # список загруженный через бд, применяем к списку функцию clean
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list,key=Group.id_or_max)  # проверка отсортированных списков
