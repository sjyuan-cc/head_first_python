# NameError
try:
    a = ''
except NameError, e:
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
