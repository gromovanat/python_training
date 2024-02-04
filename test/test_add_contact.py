# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", address="Moskovskaya st 18-15", home="+74012555555", mobile="+79114830657", work="+74012666666", fax="+74012888888",
                                email1="vanya@mail.ru", email2="vanya2@mail.ru", email3="vanya3@mail.ru", bday="1", bmonth="January", byear="2000"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)



