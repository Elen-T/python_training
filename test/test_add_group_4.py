# -*- coding: utf-8 -*-

from model.group import Group


def test_add_groupp2(app):
    # сохранение старого списка групп
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj"))
    # получение нового списка групп
    new_groups = app.group.get_group_list()
    # проверка что новый список длиннее старого
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_groupp2(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
