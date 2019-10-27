#Скрипт который устанавливает соединение с БД и извлекаем данные из БД
#import mysql.connector
# import pymysql.cursors
import pymysql

connection = pymysql.connect(host="127.0.0.1", database = "addressbook", user ="root", password = "") # устанавливаем соединение

try:
    cursor = connection.cursor()  # для создания запроса к бд нужно создать курсор, указатель на данные в бд
    cursor.execute("select * from group_list") # запрос к бд на скл
    for row in cursor.fetchall(): # в цикле проходим по всем извлеченным данным, fetchall- метод возвращает все что извлек в виде набора строк
        print(row)
finally:
    connection.close()






