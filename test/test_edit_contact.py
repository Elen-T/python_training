from model.contacts import Contacts
import random

def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contacts(firstname="for modify test_"))
    contact = Contacts(firstname="new1", middlename="new2", lastname="new3", nickname="new4")
    old_contacts = db.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    id = contact.id
    app.contact.edit_contact_by_id(contact, id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contacts.id_or_max)



"""def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(firstname="test"))
    old_contacts = app.contact.get_contact_list
    index = randrange(len(old_contacts))
    contact = Contacts(firstname="new1", middlename="new2", lastname="new3", nickname="new4")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)"""
