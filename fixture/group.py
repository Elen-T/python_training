from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group.py page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # удаление первой группы
        wd.find_element_by_name("delete").click()
        self.return_to_groups()
        self.group_cache = None

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click() #выбор нужного среди всех чекбоксов по индексу

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

    def modify_group_by_index(self,index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)     # выбор случайной группы
        wd.find_element_by_name("edit").click()  # открытие формы редактирования
        self.fill_group_form(new_group_data)   # заполнение формы
        wd.find_element_by_name("update").click()  # подтверждение обновления
        self.return_to_groups()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # сохранение группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups()
        self.group_cache = None # сброс кэша

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text): # проверка что значение кот собираемся ввести в поле ввода установлено т.е. не None
        wd = self.app.wd
        if text is not None: # если не выполняется условие, то выполнить:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        # проверка, что находимся на нужной странице и не нужен переход
        if not (wd.current_url.endswith("/group.py.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    # загрузка списка
    def get_group_list(self):
        if self.group_cache is None: # если кэш пустой, тогда нужно загрузить инфу из браузера
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group.py"):  # находим все элементы, делаем по ним цикл
                text = element.text   # получение текста, обращение к свойству text
                id = element.find_element_by_name("selected[]").get_attribute("value") # получение идентификатора
                self.group_cache.append(Group(name=text, id=id))  # по text и id построение объекта типа групп и добавление в список
        return list(self.group_cache) # возврат копии кэша (возврат получившегося сформированного списка)
