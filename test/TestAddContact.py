# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app):
   app.session.login(username="admin", password="secret")
   app.contact.create(Contacts(firstname="esryewry", middlename="weywey", lastname="weywey", nickname="weywye"))
   app.session.logout()


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
