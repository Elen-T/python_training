from model.contacts import Contacts


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(firstname="test", middlename="test", lastname="test", nickname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)