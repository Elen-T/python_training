from model.contacts import Contacts


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(firstname="test", middlename="test", lastname="test", nickname="test"))
    app.contact.edit_first_contact()