class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # удаление первой группы
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # выбор первой группы
        wd.find_element_by_name("selected[]").click()
        # нажатие редактировать первую группу
        wd.find_element_by_name("edit").click()
        # wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # wd.find_element_by_xpath("//tr[2]//td[8]//a[1]//img[1]]").click()
        # заполнениt
        # нажатие Обновить
        wd.find_element_by_name("update").click()
        self.return_to_groups()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # выбор первой группы
        self.select_first_group()
        # открытие формы редактирования
        wd.find_element_by_name("edit").click()
        # заполнение формы
        self.fill_group_form(new_group_data)
        # подтверждение обновления
        wd.find_element_by_name("update").click()
        self.return_to_groups()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # сохранение группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            # wd.find_element_by_link_text("add new").click()
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))