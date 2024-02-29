from model.contact import Contact
from random import randrange


def test_edit_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Roman", middlename="Romanovich", lastname="Romanov", bday="10")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
