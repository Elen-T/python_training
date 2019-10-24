# отдельный пакет работы с тестовыми данными для теста добавление группы
from model.group import Group
import random
import string

constant =[
     Group(name="name1", header="header1", footer="footer1"),
     Group(name="name2", header="header2", footer="footer2"),
]

def random_string(prefix,maxlen): #генерация случайных тест данных (prefix - слово с кот начинается строка,maxlen - мах длинна строки )
    symbols=string.ascii_letters + string.digits + " "*10 # это символы которые будут в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen)) ]) # random.choice случайным образом выбирает символ из строки случайной длинны - random.randrange(maxlen) (будет сгенерир случайн длинна не превыш мах) потом склеиваем этот список -"".join


testdata =[     # описываем тестовые данные  в виде генерации комбинаций
    Group(name=name, header=header, footer=footer) # строим обект типа групп , в котором параметры получаются из циклов
    for name in ["",random_string("name",10)] # переменная name пробегает по двум возможным значениям пустое или случайное, берутся комбинации типа пустое name, случайный header, пустой футер
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]

"""testdata =[ Group(name="", header="", footer="")] +[  # описываем тестовые данные (1 группа с пустыми данными и неск с непустыми )
    Group(name=random_string("name",10), header=random_string("header",20) , footer=random_string("footer",20) )
    for i in range(5)]# будет сгенерирован объект Group, содержащийслучайные данные, 5 раз и из этих сгенерированных объектов будет построен список
"""