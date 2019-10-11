from sys import maxsize


class Contacts:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        # id надо сравнивать только если они определены поэтому добавлено условие или
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        # если есть ид , то возвращается он
        if self.id:
            return int(self.id)
        else:
            return maxsize