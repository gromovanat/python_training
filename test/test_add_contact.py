# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.app_contact import AppContact

@pytest.fixture
def app(request):
    fixture = AppContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", addres="Moskovskaya st 18-15", home="+74012555555", mobile="+79114830657", work="+74012666666", fax="+74012888888",
                                email1="vanya@mail.ru", email2="vanya2@mail.ru", email3="vanya3@mail.ru", bday="1", bmonth="January", byear="2000"))
    app.session.logout()




