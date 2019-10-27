# генератор контактов
from model.contacts import Contacts
import random
import string
import os.path
import jsonpickle
import getopt # для чтения из командной строки
import sys #для получения доступа к этим опциям
# -n10 -f data/contacts.json
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])  # синтаксис из документации, n -задает кол-во генерируемых данных, f - файл в который это помещается
except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        getopt.usage()
        sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts: # синтаксис из документации, о - опция, а - ее значение, opts - переменная прочитанная парсером getopt
    if o =="-n": # если название опции -n, значит в ней задается количество групп, то есть берется значение опции и преобразуется в число
        n=int(a)
    elif o =="-f": #  если название опции -f, значит в ней задается файл
        f=a


def random_string(prefix,maxlen): #генерация случайных тест данных (prefix - слово с кот начинается строка,maxlen - мах длинна строки )
    symbols=string.ascii_letters + string.digits + " " # это символы которые будут в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen)) ]) # random.choice случайным образом выбирает символ из строки случайной длинны - random.randrange(maxlen) (будет сгенерир случайн длинна не превыш мах) потом склеиваем этот список -"".join


testdata =[ Contacts(firstname="", middlename="", lastname="", nickname="")] +[  # описываем тестовые данные (1 группа с пустыми данными и неск с непустыми )
    Contacts(firstname=random_string("firstname",10), middlename=random_string("middlename",20) , lastname=random_string("lastname",20) , nickname=random_string("nickname",20)  )
    for i in range(5)]# будет сгенерирован объект Group, содержащийслучайные данные, 5 раз и из этих сгенерированных объектов будет построен список

#сохранение сгенерированных данных в файл
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) #путь к файлу

with open(file,"w") as out: #открываем его на запись
    jsonpickle.set_encoder_options("json", indent=2)# параметры форматирования представления данных
    out.write(jsonpickle.encode(testdata))