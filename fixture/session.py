class SessionHelper: # помощник по работе с сессиями

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        wd = self.app.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def is_logged_in(self): # проверка, находимся ли внутри активной сессии, то есть есть ли на странице ссылка Logout
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username): # проверка, что вошли как нужный пользователь (по имени)
        wd = self.app.wd
        return wd.find_element_by_xpath("html[1]/body[1]/div[1]/div[1]/form[1]/b[1]").text == "("+username+")"

    def ensure_logout(self): # опреция чтобы убедииться, что вышли из системы
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password): # проверка нужен ли логин, если уже залогинены, то ничего не далать
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)