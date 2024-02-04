from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="Roman", middlename="Romanovich", lastname="Romanov", bday="10"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

