class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # выбор первой группы
        wd.find_element_by_name("selected[]").click()
        # удаление первой группы
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # выбор первой группы
        wd.find_element_by_name("selected[]").click()
        # нажатие редактировать первую группу
        wd.find_element_by_name("edit").click()
        # wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # wd.find_element_by_xpath("//tr[2]//td[8]//a[1]//img[1]]").click()
        # нажатие Обновить
        wd.find_element_by_name("update").click()
        self.return_to_groups()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        # заполнение формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # сохранение группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

    def open_groups_page(self):
        # открытие страницы групп
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_link_text("groups").click()