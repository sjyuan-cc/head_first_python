# -*- coding: utf-8 -*-

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
