from sys import maxsize


class Contacts:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None, address=None,
                 all_emails_from_home_page=None, email=None, email2=None, email3=None, home=None, mobile=None, work=None, phone2=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.all_emails_from_home_page=all_emails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.home= home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2


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