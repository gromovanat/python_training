# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", address="Moskovskaya st 18-15", home="+74012555555", mobile="+79114830657", work="+74012666666", fax="+74012888888",
                                email1="vanya@mail.ru", email2="vanya2@mail.ru", email3="vanya3@mail.ru", bday="1", bmonth="January", byear="2000")
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


