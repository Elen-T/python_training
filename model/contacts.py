class Contacts:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname