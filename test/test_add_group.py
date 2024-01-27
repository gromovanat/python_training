# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Name Group", header="Group header test", footer="footer test"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

