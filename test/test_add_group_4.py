# -*- coding: utf-8 -*-

from model.group import Group
from sys import maxsize


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
    # вычисление по группе ключа используемого для сравнения
    def id_or_max(gr):
        # если есть ид , то возвращается он
        if gr.id:
            return gr.id
        else:
            return maxsize
    # сравниваем отсортированные группы
    assert sorted(old_groups) == sorted(new_groups)


def test_add_empty_groupp2(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
