# -*- coding: utf-8 -*-
from model.contacts import Contacts

#@pytest.mark.parametrize("contact.py",testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contacts):
    contact=json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts ) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


"""testdata =[     # описываем тестовые данные  в виде генерации комбинаций
    Contacts(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname)
    for firstname in ["", random_string("firstname", 10)]
    for middlename in ["", random_string("middlename", 20)]
    for lastname in ["", random_string("lastname", 20)]
    for nickname in ["", random_string("nickname", 20)]
]"""

"""def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
      def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
      def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True"""
