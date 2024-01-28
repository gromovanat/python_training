from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="Test"))
    app.contact.edit_first_contact(Contact(firstname="Roman", middlename="Romanovich", lastname="Romanov", bday="10"))

