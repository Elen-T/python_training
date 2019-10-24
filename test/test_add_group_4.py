# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import testdata # импорт тестовых данных из отдельного пакета

@pytest.mark.parametrize("group",testdata, ids=[repr(x) for x in testdata])# с помощью этой пометки тест фрейворк передает тест данные в кач параметра в тест (в ней указ название параметра,в который передаются тест данные- group, источник тест данных - testdata и текстовое представление данных - список ids  )
def test_add_groupp2(app,group): # app - фикстура параметр тест метода, тестовые данные передаем в кач параметра теста
        old_groups = app.group.get_group_list()   # загрузка старого списка групп
        #group = Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj") # локальная переменная, содержащая добавляемую группу
        app.group.create(group) # создаем новую группу
        assert len(old_groups) + 1 == app.group.count() # проверка что новый список длиннее старого, метод count выступает в роле хэша
        new_groups = app.group.get_group_list()  # получение нового списка групп из приложения, после того как в приложение была добавлена группа
        old_groups.append(group) # старый список, в который сами добавили группу (append - в конец)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравниваем отсортированные группы по правилу key


"""def test_add_empty_groupp2(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)"""