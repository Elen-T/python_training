class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # выбор первого контакта
        wd.find_element_by_name("selected[]").click()
        # нажатие редактировать первого контакта
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # wd.find_element_by_xpath("//tr[2]//td[8]//a[1]//img[1]]").click()
        # нажатие Обновить
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # выбор первого контакта
        wd.find_element_by_name("selected[]").click()
        # удаление первого контакта
        # wd.find_element_by_name("Delete").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # закрытие диалогового окна, в котором пользователь подтверждает удаление контакта
        wd.switch_to_alert().accept()
        # self.return_home_page()

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

    def open_edit_contact_page(self):
        # открытие страницы добавления контакта
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()