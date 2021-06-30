from fixture.orm import ORMFixture
from model.group import Group
from model.contacts import Contacts

import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="1TestGroup"))
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact.id, group.id)
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.remove_contact_from_group(contact.id, group.id)
    old_contacts_in_group.remove(contact)
    new_contacts_from_group = db.get_contacts_in_group(group)

    assert sorted(old_contacts_in_group, key=Contacts.id_or_max) == sorted(new_contacts_from_group, key=Contacts.id_or_max)


"""def test_delete_contact_from_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contacts(firstname="Russel", lastname="Westbrook"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(old_groups)
    old_contacts_in_group = db.get_contacts_in_group(group)
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact, group)
    else:
        contact = random.choice(old_contacts_in_group)
    old_contacts_in_group_update = db.get_contacts_in_group(group)
    app.contact.remove_contact_from_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group_update) - 1 == len(new_contacts_in_group)
    old_contacts_in_group_update.remove(contact)
    assert sorted(old_contacts_in_group_update, key=Contacts.id_or_max) == sorted(new_contacts_in_group, key=Contacts.id_or_max)

def test_del_contact(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    group = random.choice(db.get_group_list())
    if len(db.get_contacts_not_in_group(Group(id=group.id))) == 0:
        app.contact.create(Contacts(lastname="lastname", firstname="firstname", address="address", email="email"))
    contact_not_in_group = random.choice(db.get_contacts_not_in_group(Group(id=group.id)))
    app.contact.add_contact_to_group_by_id(contact_not_in_group.id, group.id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    contact_in_group = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group_by_id(contact_in_group.id, group.id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    old_contacts_in_group.remove(contact_in_group)
    assert sorted(old_contacts_in_group, key=Contacts.id_or_max) == sorted(new_contacts_in_group, key=Contacts.id_or_max)"""