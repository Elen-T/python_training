# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list
    contact = Contacts(firstname="esryewry", middlename="weywey", lastname="weywey", nickname="weywye")
    app.contact.create(contact)
    assert len(old_contacts ) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

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
