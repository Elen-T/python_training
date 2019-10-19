from model.contacts import Contacts
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def edit_contact_by_index(self, index, new_data):
        wd = self.app.wd
        self.open_contact_home_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_name("entry")[index].find_element_by_xpath(".//img[@alt='Edit']").click()
        # wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # wd.find_element_by_xpath("//tr[2]//td[8]//a[1]//img[1]]").click()
        self.fill_form(new_data)
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None



    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click() #выбор нужного среди всех чекбоксов по индексу

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_home_page()
        self.select_contact_by_index(index)
        # удаление первого контакта
        # wd.find_element_by_name("Delete").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()  # закрытие диалогового окна, в котором пользователь подтверждает удаление контакта
        wd.find_element_by_css_selector("div.msgbox")       # ожидание загрузки элементов
        # self.return_home_page()
        self.contact_cache = None

    def delete_first_contact(self, index):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def open_contact_home_page(self):
        wd = self.app.wd
        # if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
        if not(wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("MainForm")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contacts):
        wd = self.app.wd
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
        self.return_home_page()
        self.contact_cache = None

    def open_edit_contact_page(self):
        # открытие страницы добавления контакта
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    # загрузка списка
    # @property
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):  # находим все элементы, делаем по ним цикл
                cells = row.find_elements_by_tag_name("td")      # получение текста, обращение к свойству
                firstname = cells[1].text
                lastname = cells[2].text
                #id = element.find_element_by_name("selected[]").get_attribute("value")  # получение идентификатора
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contacts(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
                # all_phones = cells[5].text.splitlines()  # из ячейки читаются только все телефоны, полученную строку разрезаем на части(берем текст из ячейки и делим на (text.splitlines))
                # self.contact_cache.append(Contacts(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page = all_phones, homephone=all_phones[0],mobilephone=all_phones[1], workphone=all_phones[2],secondaryphone=all_phones[3]))   # по text и id построение объекта типа контакт и добавление в список
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):  # новый
        wd = self.app.wd
        self.open_contact_home_page()
        # self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index): # новый
        wd = self.app.wd
        self.open_contact_home_page()
        # self.app.open_home_page()
        row =  wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index): # открываем форму редактирования, читаем из нее инфу
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contacts(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                        mobilephone=mobilephone, secondaryphone=secondaryphone)  # построение объекта из этих данных

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text=wd.find_element_by_id("content").text # извлечение текста из страницы просмотра контакта
        homephone = re.search("H: (.*)", text).group(1) # рег выражения для извлечения номера телефона из текста страницы просмотра
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contacts(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                        secondaryphone=secondaryphone)  # построение объекта из этих данных


