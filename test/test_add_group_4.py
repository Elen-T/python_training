# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix,maxlen): #генерация случайных тест данных (prefix - слово с кот начинается строка,maxlen - мах длинна строки )
    symbols=string.ascii_letters + string.digits + " "*10 # это символы которые будут в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen)) ]) # random.choice случайным образом выбирает символ из строки случайной длинны - random.randrange(maxlen) (будет сгенерир случайн длинна не превыш мах) потом склеиваем этот список -"".join


testdata =[     # описываем тестовые данные  в виде генерации комбинаций
    Group(name=name, header=header, footer=footer) # строим обект типа групп , в котором параметры получаются из циклов
    for name in ["",random_string("name",10)] # переменная name пробегает по двум возможным значениям пустое или случайное, берутся комбинации типа пустое name, случайный header, пустой футер
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


@pytest.mark.parametrize("group",testdata, ids=[repr(x) for x in testdata])# с помощью этой пометки тест фрейворк передает тест данные в кач параметра в тест (в ней указ название параметра,в который передаются тест данные- group, источник тест данных - testdata и текстовое представление данных - список ids  )
def test_add_groupp2(app,group): # app - фикстура параметр тест метода, тестовые данные передаем в кач параметра теста
        old_groups = app.group.get_group_list()   # загрузка старого списка групп
        #group = Group(name="fgjfgj", header="fgjfgj", footer="fgjfgj") # локальная переменная, содержащая добавляемую группу
        app.group.create(group) # создаем новую группу
        assert len(old_groups) + 1 == app.group.count() # проверка что новый список длиннее старого, метод count выступает в роле хэша
        new_groups = app.group.get_group_list()  # получение нового списка групп из приложения, после того как в приложение была добавлена группа
        old_groups.append(group) # старый список, в который сами добавили группу (append - в конец)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравниваем отсортированные группы по правилу key

"""testdata =[ Group(name="", header="", footer="")] +[  # описываем тестовые данные (1 группа с пустыми данными и неск с непустыми )
    Group(name=random_string("name",10), header=random_string("header",20) , footer=random_string("footer",20) )
    for i in range(5)]# будет сгенерирован объект Group, содержащийслучайные данные, 5 раз и из этих сгенерированных объектов будет построен список
"""

"""def test_add_empty_groupp2(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)"""