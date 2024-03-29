from sys import maxsize


class Group:
    def __init__ (self, name=None, header=None, footer=None, id=None):
        #запись значений параметров в свойства объекта
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self): #спец функция, определяет как будет выглядеть объект при выводе на консоль
        return "%s:%s:%s:%s" % (self.id, self.name, self.header,self.footer)

    def __eq__(self, other): # сравнение текущего обьекта с новым other
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name #  группы равны если совпадают имена, и также совпад ид либо у одной из них неопределен

    # вычисление по группе ключа используемого для сравнения
    def id_or_max(self):
        if self.id:
            return int(self.id)  # если есть ид , то возвращается он
        else:
            return maxsize     # если нет ид , то возвращается мах число