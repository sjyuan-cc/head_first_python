# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

import datetime

import functools


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r

    return fn


@performance
def factorial(n):
    time.sleep(3)
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)


def log(fn):
    def decorate(*arg, **kwargs):
        print 'call %s() in at %s' % (fn.__name__, datetime.datetime.today())
        fn(*arg, **kwargs)

    return decorate


@log
def say():
    print 'hello python'


print datetime.datetime.strptime('2015-10-10 08:08:08', '%Y-%m-%d %H:%M:%S')


def performance(unit):
    def decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            r = fn(*args, **kwargs)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit is 'ms' else (t2 - t1)
            print 'call %s() in %f %s' % (fn.__name__, t, unit)
            return r

        return wrapper

    return decorate


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial.__name__

print cmp(3, 3)

sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])


def boy_marry(fn):
    def wrapper():
        return fn(sex='Boy')

    return wrapper


def girl_marry(fn):
    def wrapper():
        return fn(sex='Girl')

    return wrapper


def marry(sex):
    if sex is 'Boy':
        print 'He will be a husband.'
    elif sex is 'Girl':
        print 'She will be a wife.'


bm = boy_marry(marry)
fm = boy_marry(marry)
bm()
fm()

bm = functools.partial(marry, sex='Boy')
gm = functools.partial(marry, sex='Girl')
bm()
gm()

print __name__

s = 'Am I an unic你好?'
print isinstance(s, unicode)
print 10 / 3
