NameError
try:
    a
except (NameError, KeyError), e:
    print 'aaaaa', e
else:
    print 'else'
finally:
    print 'finally'

# # SyntaxError
# if True
#
# # IOError
# file = open('test.txt')
#
# # ZeroDivisionError
# print 10 / 0
#
# # ValueError
# print int('a')
#
# from time import sleep
#
# # KeyboardInterrupt
# for i in range(10):
#     sleep(3)  # after interrupted,
#
from contextlib import contextmanager

# with open('exception_test.txt') as f:
#     print f.readline()
#
# print 'file is closed = %s' % f.closed

f = open('exception_test.txt')
try:
    print f.readline()
finally:
    f.close() if f else None


class MyFile(object):
    def __init__(self, name):
        print '__init__'
        self.file = open(name)

    def __enter__(self):
        print '__enter__'
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__'
        print 'Error=%s, Value=%s, exc_tb=%s' % (exc_type, exc_val, exc_tb)
        self.file.close()
        print self.file.closed
        # if True, exception will be ignored


with MyFile('exception_test.txt') as f1:
    for line in f1:
        print line


@contextmanager
def my_file(file_name):
    print 'open a file'
    opened_file = open(file_name)

    try:
        yield opened_file
    except StandardError:
        opened_file.close()
        print 'closed=%s' % opened_file.closed


with my_file('exception_test.txt') as active_file:
    for line in active_file:
        print line

# print active_file.closed
