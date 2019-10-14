from model.group import Group
from random import randrange


def test_delete_some_group(app):  # удаление группы, выбранной случайным образом
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
