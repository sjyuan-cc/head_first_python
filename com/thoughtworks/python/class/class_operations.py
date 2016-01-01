class Person(object):
    def __init__(self, name, sex, birthday, **kwargs):
        self.name = name
        self.sex = sex
        self.birthday = birthday
        print kwargs
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job


class Person1(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def __test(self):
        print self


p = Person1('Bob', 59)

print p.name


class Person(object):
    count = 0

    def __init__(self, name):
        Person.count += 1


p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count


class Person(object):
    __count = 0

    def __init__(self, name):
        self.name = name
        Person.__count += 1


p1 = Person('Bob')
p2 = Person('Alice')

import types


def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
# print p2.get_grade()

import json


class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'


s = Students()

print json.load(s)


class Person(object):
    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    __slots__ = ('name', 'gender', 'score')

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score


class Fib(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a = b
            b = a + b
            a, b = b, a + b
        return L


f = Fib()
print f(10)
