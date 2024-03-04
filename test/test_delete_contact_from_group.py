import random
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

data_base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
    # если нет группы - создать группу
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # если нет контакта - создать контакт
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Test"))
    # выбрать любую группу из списка существующих групп
    group_list = app.group.get_group_list()
    random_group = random.choice(group_list)
    # получить имя и id выбранной группы
    group_name = random_group.name
    group_id = random_group.id
    # если в группе нет контакта - добавить его в группу
    if len(data_base.get_contacts_in_group(Group(id=group_id))) == 0:
        app.contact.contact_add_to_group(0, group_name)
    # получаем список контактов в группе:
    contacts_list_in_group = app.contact.get_contact_list_in_group(group_name)
    # выбираем рандомный контакт
    random_contact = random.choice(contacts_list_in_group)
    index = contacts_list_in_group.index(random_contact)
    # удаляем рандомный контакт из списка в группе
    app.group.delete_contact_from_group(index, group_name)
    # проверяем, что контакт удалился из группы в БД
    l = data_base.get_contacts_not_in_group(Group(id=group_id))
    assert random_contact.id  in [x.id for x in l]
