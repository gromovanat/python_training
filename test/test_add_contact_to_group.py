import random
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

data_base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    # если нет группы - создать группу
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # из списка групп выбираем рандомную и узнаем ее id
    group_list = app.group.get_group_list()
    random_group = random.choice(group_list)
    group_id = random_group.id
    # если нет ни одного контакта, который не входит в выбранную группу,- создать новый контакт
    if len(data_base.get_contacts_not_in_group(Group(id=group_id))) == 0:
        app.contact.create_new_contact(Contact(firstname="Test"))
    # получаем список контактов, не входящих в группу
    n = data_base.get_contacts_not_in_group(Group(id=group_id))
    # из списка контактов, не входящих в группу, выбираем рандомный
    random_contact = random.choice(n)
    #узнаем его индекс
    id_contact = random_contact.id
    # выбираем в ui контакт по id и добавляем его в группу по id
    app.contact.contact_add_to_group(id_contact, group_id)
    # Проверяем, что контакт входит в группу: контакт с таким id есть в списке группы?
    l = data_base.get_contacts_in_group(Group(id=group_id))
    assert random_contact.id in [x.id for x in l]
