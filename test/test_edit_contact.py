from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.edit_first_contact(Contact(firstname="Roman", middlename="Romanovich", lastname="Romanov", addres="Leningradskaya st 20-1", home="+74012444444", mobile="+79114967012", work="+74012888888", fax="+74012111111",
                                email1="roma@mail.ru", email2="roma2@mail.ru", email3="roma3@mail.ru", bday="10", bmonth="May", byear="1988"))
    app.session.logout()