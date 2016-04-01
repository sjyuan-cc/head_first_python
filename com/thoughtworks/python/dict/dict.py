from itertools import groupby
from operator import itemgetter

contacts = {'sjyuan': 18192235667}

contacts = dict(sjyuan=18192235667)

contacts = dict([('sjyuan', 18192235667)])

contacts = dict(zip(['bfeng', 'sjyuan'], [18156965336, 18192235667]))

contacts = dict.fromkeys(('sjyuan', 'bofeng'), None)

print contacts

try:
    a = ''
except NameError, e:
    print 'aaaaa', e
else:
    print 'else'
finally:
    print 'finally'

contacts = {'1': 2}
print '======%(1)s' % contacts

for i in range(100):
    if i == 10:
        continue

a = [{'a': 1, 'b': 1}, {'a': 1, 'b': 2}, {'a': 1, 'b': 5}]

res = groupby(a, key=itemgetter('a'))
print res

for k, v in res:
    print v
    print k, list(v)
    for i in v:
        print i, type(i)
