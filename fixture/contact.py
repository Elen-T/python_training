from model.contacts import Contacts


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
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):  # находим все элементы, делаем по ним цикл
                # получение текста, обращение к свойству
                lastname_text = element.find_elements_by_tag_name("td")[1].text
                firstname_text = element.find_elements_by_tag_name("td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")  # получение идентификатора
                # по text и id построение объекта типа контакт и добавление в список
                self.contact_cache.append(Contacts(lastname=lastname_text, firstname=firstname_text, id=id))
            return list(self.contact_cache)



