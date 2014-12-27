__author__ = 'seandolinar'
<<<<<<< Updated upstream
__version__ = 1.0


=======
__version__ = 2.0
>>>>>>> Stashed changes

import __builtin__


class Book(object):
    def __init__(self, title=None, author=None, genre=None,check_out=0):
        self.title = title
        self.author = author
        self.check_outs = check_out
        self.status = 'AVAIL'
        self.genre = genre

    def check_out(self):
        if self.status == 'AVAIL':
            self.check_outs += 1
            self.status = 'OUT'
        else:
            print 'This book is already checked out'
        return

    def check_in(self):
        if self.status == 'OUT':
            self.status = 'AVAIL'
        else:
            print 'This book is already checked in'
        return

    def __str__(self):
        return self.title +' by ' + self.author + '.  It is ' +  self.status + '.'


class ChildrensBook(Book):
    def __init__(self, title, author, check_out, grade_level=1, school_project = False):
        Book.__init__(self, title, author, 'Childrens', check_out)
        self.grade_level = grade_level
        self.school_project = school_project

    def reserve(self):
        self.school_project = True

    def unreserve(self):
        self.school_project = False


class SuperString(str):
    def find_i(self):
        counter = 0
        for i in self:
            if 'i' == i:
                counter += 1
        return counter














__builtin__.str = SuperString


a = str('hiiiiiiiiiiii')






print type(a)

print Book('Hunt for Red October', 'Tom', 'Spy', 0)
book1 = ChildrensBook('Cat in the Hat', 'Suess', 0)

for i in range(1,5):
    book1.check_out()
    book1.check_in()

print book1.check_outs

