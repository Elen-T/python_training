from model.contacts import Contacts


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contacts(firstname="new1", middlename="new2", lastname="new3", nickname="new4")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
