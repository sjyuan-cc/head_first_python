class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        return cmp(s.score, self.score) if cmp(s.score, self.score) is not 0 else cmp(self.name, s.name)


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)
