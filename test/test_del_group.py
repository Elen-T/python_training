from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):  # удаление группы, выбранной случайным образом, check_ui - новая фикст
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group= random.choice(old_groups) # поиск нужной группы и удаление ее по ид, в качестве параметра список из кот нужно выбрать случайный элемент
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list() # новый список получен из бд, в кот была удалена первая группа
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group) # удаление старого элемента из списка
    assert old_groups == new_groups
    if check_ui:          # если выполняется условие, выставлен флаг check , то делается следующая проверка
        assert sorted (new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max) # сравниваем список загруженный из БД и приложения


"""def test_delete_some_group(app):  # удаление группы, выбранной случайным образом
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange (len(old_groups)) # определение индекса удаляемой группы
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list() # новый списоек получен из приложения, в кот была удалена первая группа
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    # old_groups[0:1] = [] # делаем вырезку, в старом списке удаляем все элементы с 0 по 1 (т.е. один элемент с индесом 0)
    assert old_groups == new_groups
"""