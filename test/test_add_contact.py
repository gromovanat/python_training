# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits_string(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


def random_letters_string(prefix, maxlen):
    letters = string.ascii_letters + " "*2
    return prefix + "".join([random.choice(letters) for i in range(random.randrange(maxlen))])


def random_email():
    symbols_for_mail_name = string.ascii_letters + string.digits + "." + "-" + "_"
    generated_mail_name = ''.join([random.choice(symbols_for_mail_name) for i in range(random.randrange(1, 15))])
    generated_domain_name = ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 10))])
    generated_main_domain = ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 5))])
    random_emails = f"{generated_mail_name}@{generated_domain_name}.{generated_main_domain}"
    return random_emails


testdata = [Contact(firstname=random_letters_string("firstname", 10), lastname=random_letters_string("lastname", 10),
                    address=random_string("address", 30),
                    home=random_digits_string(11), mobile=random_digits_string(11), work=random_digits_string(11),
                                email1=random_email(), email2=random_email(), email3=random_email())]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


