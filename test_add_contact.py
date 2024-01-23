# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from contact import Contact
from app_contact import AppContact

@pytest.fixture
def app(request):
    fixture = AppContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username = "admin", password = "secret")
    app.open_new_contact_page()
    app.create_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", addres="Moskovskaya st 18-15", home="+74012555555", mobile="+79114830657", work="+74012666666", fax="+74012888888",
                                email1="vanya@mail.ru", email2="vanya2@mail.ru", email3="vanya3@mail.ru", bday="1", bmonth="January", byear="2000"))
    app.returt_to_home_page()
    app.logout()




