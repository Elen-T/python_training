from model.contacts import Contacts
import random

def test_delete_some_contact(app, db, check_ui):
    if len (db.get_contact_list()) == 0:
        app.contact.create(Contacts(firstname="test", middlename="test", lastname="test", nickname="test"))
    old_contacts = db.get_contact_list()
    contact= random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

