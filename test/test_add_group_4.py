# -*- coding: utf-8 -*-

from model.group import Group


def test_add_groupp2(app): # app - фикстура параметр тест метода
    old_groups = app.group.get_group_list()   # загрузка старого списка групп
    group = Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj") # локальная переменная, содержащая добавляемую группу
    app.group.create(group) # создаем новую группу
    assert len(old_groups) + 1 == app.group.count # проверка что новый список длиннее старого, метод count выступает в роле хэша
    new_groups = app.group.get_group_list()  # получение нового списка групп из приложения, после того как в приложение была добавлена группа
    old_groups.append(group) # старый список, в который сами добавили группу (append - в конец)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравниваем отсортированные группы по правилу key


def test_add_empty_groupp2(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)