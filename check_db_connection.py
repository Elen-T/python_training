#Скрипт который устанавливает соединение с БД и извлекаем данные из БД
#import mysql.connector
# import pymysql.cursors
import pymysql
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name = "addressbook", user ="root", password = "") # будет создаваться новый объект типа DbFixture
#connection = pymysql.connect(host="127.0.0.1", database = "addressbook", user ="root", password = "") # устанавливаем соединение

try: # вывод инфы на консоль
    l = db.get_contacts_not_in_group(Group(id="233"))
    for item in l:
        print(item)
    print(len(l)) #печатаем длинну списка
finally:
     pass # db.destroy()


"""try: # вывод инфы на консоль
    l = db.get_contacts_in_group(Group(id="230"))
    for item in l:
        print(item)
    print(len(l)) #печатаем длинну списка
finally:
     pass # db.destroy()"""

"""try: 
    cursor = connection.cursor()  # для создания запроса к бд нужно создать курсор, указатель на данные в бд
    cursor.execute("select * from group_list") # запрос к бд на скл
    for row in cursor.fetchall(): # в цикле проходим по всем извлеченным данным, fetchall- метод возвращает все что извлек в виде набора строк
        print(row)"""




