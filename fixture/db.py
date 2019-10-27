import pymysql
from model.group import Group

class DbFixture:

    def __init__(self, host, name, user, password):
       self.host = host # присваеваем переданные значения в поля созданного объекта
       self.name = name
       self.user = user
       self.password = password
       self.connection = pymysql.connect(host=host, database = name, user = user, password = password) # устанавливаем соединение

    def get_group_list(self):# загрузка из бд инфы о группах из таблицы group_list
        list = []  # список для объекта
        cursor = self.connection.cursor() # запрос к бд на скл
        try:
            cursor.execute("select group_id,group_name, group_header, group_footer from group_list") #выполнение запроса
            for row in cursor:
                (id, name, header, footer) = row # тк каждая из строк таблицы это кортеж, т.е. присвоить значения сразу в 4 перременные
                list.append(Group(id=id,name=name, header=header,footer=footer ))# строим новый объект  и помещаем его в список
        finally:   # закрытие запроса
            cursor.close()
        return list

    def destroy(self):
        self.connection.close() # разрываем соединение