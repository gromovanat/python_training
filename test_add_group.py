# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
import warnings
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group(name="Name Group", header="Group header test", footer="footer test"))
    app.logout()


def test_add_empty_group(app):
    app.login( "admin", "secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()




