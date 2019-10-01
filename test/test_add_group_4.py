# -*- coding: utf-8 -*-

from model.group import Group


def test_add_groupp2(app):
    app.group.create(Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj"))


def test_add_empty_groupp2(app):
    app.group.create(Group(name="", header="", footer=""))
