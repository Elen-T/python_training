from model.contacts import Contacts
from model.group import Group
from fixture.orm import ORMFixture
import random

dbase = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contacts(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    contacts_in_group = dbase.get_contacts_in_group(group)
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    app.contact.add_contact_to_group(contact, group)
    contacts_in_group.append(contact)
    assert sorted(contacts_in_group, key=Contacts.id_or_max) == sorted(dbase.get_contacts_in_group(group), key=Contacts.id_or_max)

def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contacts(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    contacts_in_group = dbase.get_contacts_in_group(group)
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    if contact in dbase.get_contacts_not_in_group(group):
        app.contact.add_contact_to_group(contact, group)
        contacts_in_group = dbase.get_contacts_in_group(group)
    app.contact.remove_contact_from_group(contact, group)
    contacts_in_group.remove(contact)
    assert sorted(contacts_in_group, key=Contacts.id_or_max) == sorted(dbase.get_contacts_in_group(group), key=Contacts.id_or_max)