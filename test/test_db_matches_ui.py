#тест для проверки соответствия списка групп выгруженного из БД и из приложения
from model.group import Group


def tes_group_list(app, db):        # передаем два параметра app - для получения доступа к приложению, db - фикстура для получения доступа к бд
   ui_list = app.group.get_group_list()        # сравниваем результаты, список загруженный через приложение
   db_list = db.get_group_list()  # список загруженный через бд
   assert  sorted(ui_list, key=Group.id_or_max) ==sorted(db_list, key=Group.id_or_max) # проверка отсортированных списков