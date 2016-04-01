for i in range(1, 101):
    if i % 7 == 0:
        print i

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name

L = ['Adam', 'Lisa', 'Bart', 'Paul']
orders = range(1, len(L) + 1)
print zip(orders, L)

for index, name in zip(orders, L):
    print index, '-', name

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0
for score in d.itervalues():
    sum += score
print sum / len(d)

print range(1, 11, 2)

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0
for k, v in d.iteritems():
    sum += v
    print k, ':', v
print 'average', ':', sum / len(d)

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}

for k in d.iterkeys():
    print k


def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


def new_fn(f):
    def g(x):
        print '----------------'
        return f(x)

    return g


@new_fn
def f1(x):
    return x * 2


print f1(3)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

a = [x for x in range(1000) if x % 2 == 0]
print reversed(a)

