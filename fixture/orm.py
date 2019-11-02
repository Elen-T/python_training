# новая фикстура, ORM - для взаимод с БД без скл запросов, устанавливает соответствие между классами питона и таблицами в БД, меж полями объекта и полями в бд
from datetime import datetime
from pony.orm import *
from model.group import Group
from model.contacts import Contacts
from pymysql.converters import decoders


class ORMFixture:

    db = Database() # объект на основании которого строим привязку, которая описывается в виде набора классов

    class ORMGroup(db.Entity): # описываем набор свойств и привязываем к полям таблицы бд, db.Entity - вложенный класс для привязки класса к бд
        _table_='group_list' # тут указывается название таблицы
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name') # Optional - необязательное
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True) #группа может ссылаться на несколько контактов, Set - множество, тип объектов (лямбда возвращает класс)
                                                                                    # связь при помощи табл address_in_groups, id - столбец в котором ид контактов
    class ORMContact(db.Entity): # ORMGroup наследуется от db.Entity
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')# свойство необходимое для фильтрации
        groups = Set(lambda: ORMFixture.ORMGroup,  table="address_in_groups", column="group_id",  reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):# привязка к БД в конструкторе, при помощи метода bind
        self.db.bind('mysql', host=host, database = name, user = user, password = password) #1ый параметр - тип бд, дальше набор параметров такойже как при инициализации коннектора
        self.db.generate_mapping() # с помощью этого метода происходит сопоставление свойств описанных в классе с полями таблиц бд
        sql_debug(True)

    def convert_groups_to_model(self, groups): # преобразуем объект при помощи map
        def convert(group): # конвертируем одну группу, из объекта ормгрупп построили объект типа групп
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer )
        return list(map (convert, groups)) # применение convert ко всем элементам списка

    @db_session # пометка что объектвыполняется в рамках сессии
    def get_group_list(self): # функции кот получают списки объектов
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup)) # выборка из объектов данного класса, преобразованная в список

    def convert_contacts_to_model(self, contacts): # преобразуем объект при помощи map
        def convert(contact): # конвертируем одну группу, из объекта ормгрупп построили объект типа групп
            return Contacts(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map (convert, contacts)) # применение convert ко всем элементам списка

    @db_session
    def get_contact_list(self): # функции кот получают списки объектов
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None )) # выборка из объектов данного класса, преобразованная в список

    @db_session
    def get_contacts_in_group(self, group):# получение списка контактов которые входят в группу
        orm_group=list(select (g for g in ORMFixture.ORMGroup if g.id ==group.id))[0]# у возвращенного списка берем 1ый элемент
        return self.convert_contacts_to_model(orm_group.contacts) # преобразование орм контактов в модельные

    @db_session
    def get_contacts_not_in_group(self, group):    # получение списка контактов кот не входят в заданную группу
        orm_group=list(select (g for g in ORMFixture.ORMGroup if g.id ==group.id))[0]# у возвращенного списка берем 1ый элемент
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups)) # выборка из объектов данного класса, преобразованная в список
