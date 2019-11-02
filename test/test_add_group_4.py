# -*- coding: utf-8 -*-
from model.group import Group
from data.groups import testdata # импорт тестовых данных из отдельного пакета

def test_add_groupp2(app, db, json_groups): # добавлена параметризация, читает данные изфайла groups.json
        group=json_groups
        old_groups = db.get_group_list()  # загрузка старого списка групп из бд
        app.group.create(group) # создаем новую группу
        new_groups = db.get_group_list()  #
        old_groups.append(group) # старый список, в который сами добавили группу (append - в конец)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравниваем отсортированные группы по правилу key



"""def test_add_groupp2(app, json_groups): # app - фикстура параметр тест метода, тестовые данные передаем в кач параметра теста, data_groups - указывает что тест данные загружаются из фикстуры с префиксом json
        group=json_groups
        old_groups = app.group.get_group_list()   # загрузка старого списка групп #group.py = Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj") # локальная переменная, содержащая добавляемую группу
        app.group.create(group) # создаем новую группу
        assert len(old_groups) + 1 == app.group.count() # проверка что новый список длиннее старого, метод count выступает в роле хэша
        new_groups = app.group.get_group_list()  # получение нового списка групп из приложения, после того как в приложение была добавлена группа
        old_groups.append(group) # старый список, в который сами добавили группу (append - в конец)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравниваем отсортированные группы по правилу key


# @pytest.mark.parametrize("group.py",testdata, ids=[repr(x) for x in testdata])# с помощью этой пометки тест фрейворк передает тест данные в кач параметра в тест (в ней указ название параметра,в который передаются тест данные- group.py, источник тест данных - testdata и текстовое представление данных - список ids  )"""

"""def test_add_empty_groupp2(app):
    old_groups = app.group.py.get_group_list()
    group.py = Group(name="", header="", footer="")
    app.group.py.create(group.py)
    new_groups = app.group.py.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group.py)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)"""