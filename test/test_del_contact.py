from model.contacts import Contacts


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contacts(firstname="test", middlename="test", lastname="test", nickname="test"))
    app.contact.delete_first_contact()
