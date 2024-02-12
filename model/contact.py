from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, address=None, home=None, mobile=None,
                 work=None, fax=None, email1=None, email2=None, email3=None, bday=None, bmonth=None,
                 byear=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and
                self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
