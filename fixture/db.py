# фикстура для работы с БД
import pymysql
from model.group import Group
from model.contacts import Contacts

class DbFixture:

    def __init__(self, host, name, user, password):
       self.host = host # присваеваем переданные значения в поля созданного объекта
       self.name = name
       self.user = user
       self.password = password
       self.connection = pymysql.connect(host=host, database = name, user = user, password = password, autocommit=True ) # устанавливаем соединение, доп параметр autocommit=True для сброски кэша после каждого запроса

    def get_group_list(self):# загрузка из бд инфы о группах из таблицы group_list
        list = []  # список для объекта
        cursor = self.connection.cursor() # запрос к бд на скл
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list") #выполнение запроса
            for row in cursor:
                (id, name, header, footer) = row # тк каждая из строк таблицы это кортеж, т.е. присвоить значения сразу в 4 перременные
                list.append(Group(id=str(id),name=name, header=header,footer=footer ))# строим новый объект  и помещаем его в список
        finally:   # закрытие запроса
            cursor.close()
        return list

    def get_contact_list(self):  # загрузка из бд инфы о контактах из таблицы group_list
        list = []  # список для объекта
        cursor = self.connection.cursor()  # запрос к бд на скл
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")  # выполнение запроса извлечение данных
            for row in cursor:
                (id, firstname, lastname) = row  # тк каждая из строк таблицы это кортеж, т.е. присвоить значения сразу в 4 перременные
                list.append(Contacts(id=str(id), firstname=firstname, lastname=	lastname))  # строим новый объект  и помещаем его в список
        finally:  # закрытие запроса
            cursor.close()
        return list

    def get_contact_by_id(self, id_cont):
        list_cont = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, home, work, phone2, email, email2, email3 "
                           "from addressbook where deprecated = '0000-00-00 00:00:00' and id='%s'" % id_cont)
            for row in cursor:
                (id, firstname, lastname, address, mobile, home, work, phone2, email, email2, email3) = row
                list_cont.append(Contacts(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                        mobile=mobile, home=home, work=work, phone2=phone2, email=email, email2=email2,
                                        email3=email3))
        finally:
            cursor.close()
        return list_cont

    def destroy(self):
        self.connection.close() # разрываем соединение

    def get_groups_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (id) = row
                list.append(Group(id=str(id)))
        finally:
            cursor.close()
        return list



