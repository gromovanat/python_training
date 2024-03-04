from model.contact import Contact
from random import randrange

#сравнение через БД
def test_contact_on_home_page_and_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert contact_from_home_page == contact_from_db
    for index,home_contact in enumerate(contact_from_home_page):
        assert home_contact.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_db[index])
        assert home_contact.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(
            contact_from_db[index])


#сравнение через интерфейс
def test_contact_info_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
