from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contacts):
        wd = self.wd
        self.open_edit_contact_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
           # "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        self.return_home_page()

    def open_edit_contact_page(self):
        # открытие страницы добавления контакта
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()
