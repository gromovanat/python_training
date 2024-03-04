import random
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

data_base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    # если нет контакта - создать контакт
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Test"))
    # если нет группы - создать группу
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # из списка контактов выбираем рандомный и узнаем его индекс
    contacts_list = app.contact.get_contact_list()
    random_contact = random.choice(contacts_list)
    index = contacts_list.index(random_contact)
    # из списка групп выбираем рандомную и узнаем ее id
    group_list = app.group.get_group_list()
    random_group = random.choice(group_list)
    group_id = random_group.id
    # выбираем контакт по индексу и добавляем в группу по id
    app.contact.contact_add_to_group(index, group_id)
    # Проверяем, что контакт входит в группу: контакт с таким id есть в списке группы?
    l = data_base.get_contacts_in_group(Group(id=group_id))
    assert random_contact.id in [x.id for x in l]
