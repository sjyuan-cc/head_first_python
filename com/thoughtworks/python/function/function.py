# coding=utf-8

def format_name(s):
    """ format name """
    return s.upper()


print(map(format_name, ['adam', 'LISA', 'barT']))

print('\(~_~)/ \(~_~)/')

print('''line1
line2''')

print(r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.''')

print('''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.''')

print u'''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''

import math


def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x


print filter(is_sqr, range(1, 101))

print filter(lambda x: int(math.sqrt(x)) * int(math.sqrt(x)) == x, range(1, 101))


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print sorted(['bob', 'about', 'Zoo', 'Credit'], lambda s1, s2: -1 if s1.upper() < s2.upper() else 1)

print (lambda x: x + 5)(3)

a = [1]
b = [(2, 2), (3, 3)]
print a
print b
map(lambda x: a.extend(x), b)
print a


def var_args(*args):
    for arg in args:
        print arg


var_args(*[1, 2, 9])


def test(a, b=None, *args, **kargs):
    pass


a1 = 288000
b1 = 288000
print a1 is b1


class Is(object):
    def __str__(self):
        return '========='

    def __eq__(self, other):
        return True


a = Is()
b = Is()
print 'a is b : ', a is b
print 'a == b : ', a == b
print a

print'''Hello: 
Happy new year'''

aa = {}
i = Is()
aa[i] = 5555
print aa[i]

# -*- coding: utf-8 -*-
print '''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''


def count():
    val = 9

    def func():
        return val * val

    return func


f1 = count()
print f1()


def count():
    funcs = []
    for val in range(1, 4):
        def f():
            return val * val

        funcs.append(f)
    return funcs


f1, f2, f3 = count()
print f1(), f2(), f3()  # 9 9 9


def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y

        return reduce(f, lst)

    return lazy_prod


f = calc_prod([1, 2, 3, 4])
print f()


def post_process(fun, numbers):
    return [fun(number) for number in numbers]


print post_process(lambda x: x * x, [1, 2, 3, 4])


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print sorted(['bob', 'about', 'Zoo', 'Credit'], lambda s1, s2: -1 if s1.upper() < s2.upper() else 1)
