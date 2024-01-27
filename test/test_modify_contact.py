from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Roman", middlename="Romanovich", lastname="Romanov", bday="10"))

