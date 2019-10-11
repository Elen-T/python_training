# -*- coding: utf-8 -*-

from model.group import Group


def test_add_groupp2(app):
    # сохранение старого списка групп
    old_groups = app.group.get_group_list()
    group = Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj")
    app.group.create(group)
    # получение нового списка групп
    new_groups = app.group.get_group_list()
    # проверка что новый список длиннее старого
    assert len(old_groups) + 1 == len(new_groups)
    # добавление группы в список
    old_groups.append(group)

    # сравниваем отсортированные группы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_groupp2(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)