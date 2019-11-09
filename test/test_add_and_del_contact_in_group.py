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
    if contact in contacts_in_group:
        app.contact.remove_contact_from_group(contact, group)
        contacts_in_group = dbase.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    contacts_in_group.append(contact)
    assert sorted(contacts_in_group, key=Contacts.id_or_max) == sorted(dbase.get_contacts_in_group(group), key=Contacts.id_or_max)

def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contacts(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_groups_with_contacts())==0:
        contact_id = random.choice(db.get_contact_list()).id
        group_id = random.choice(db.get_group_list()).id
        app.contact.add_contact_to_group(contact_id, group_id)
    group_id = random.choice(db.get_groups_with_contacts()).id
    contact_id = random.choice(dbase.get_contacts_in_group(Group(id=group_id))).id
    app.contact.remove_contact_from_group(group_id)
    assert db.get_contact_by_id(contact_id) not in dbase.get_contacts_in_group(Group(id=group_id))

    '''if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contacts(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    contacts_in_group = dbase.get_contacts_in_group(group)
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    #if contact in dbase.get_contacts_not_in_group(group):
    #    app.contact.add_contact_to_group(contact, group)
     #   contacts_in_group = dbase.get_contacts_in_group(group)

    app.contact.remove_contact_from_group(contact, group)
    contacts_in_group.remove(contact)
    assert sorted(contacts_in_group, key=Contacts.id_or_max) == sorted(dbase.get_contacts_in_group(group),
                                                                      key=Contacts.id_or_max)'''

