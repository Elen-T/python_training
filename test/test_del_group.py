from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list() # новый списоек получен из приложения, в кот была удалена первая группа
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = [] # делаем вырезку, в старом списке удаляем все элементы с 0 по 1 (т.е. один элемент с индесом 0)
    assert old_groups == new_groups
