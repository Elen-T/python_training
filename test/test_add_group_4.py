# -*- coding: utf-8 -*-

from model.group import Group


def test_add_groupp2(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj"))
    app.session.logout()


def test_add_empty_groupp2(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
