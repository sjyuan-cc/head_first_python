import os
import sys

data = open('sketch.txt')

for line in data:
    if not line.find(':') == -1:
        (actor, msg) = line.split(":", 1)
        print(actor),
        print(' said : '),
        print msg
data.close()

if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    for line in data:
        if not line.find(':') == -1:
            (actor, msg) = line.split(":", 1)
            print(actor),
            print(' said : '),
            print msg
    data.close()

try:
    data = open('sketch1.txt')
    for line in data:
        try:
            (actor, msg) = line.split(":", 1)
            print(actor),
            print(' said : '),
            print msg
        except ValueError:
            pass
    data.close()
except IOError:
    print('File does not exist!')

man = []
other = []
try:
    data = open('sketch.txt')
    for line in data:
        try:
            (actor, msg) = line.split(":", 1)
            msg = msg.strip()
            if actor == 'Man':
                man.append(msg)
            elif actor == 'Other Man':
                other.append(msg)
        except ValueError:
            pass
    man_file = open('man_file.txt', 'w')
    other_file = open('other_file.txt', 'w')
    print >> man_file, man
    print >> other_file, other
except IOError as error:
    print('File does no  exist! error : \n' + str(error))
finally:
    if 'data' in locals():
        data.close()
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()


def print_list(books_list, intent=False, level=0, fh=sys.stdin):
    for sub_list in books_list:
        if isinstance(sub_list, list):
            print_list(sub_list, intent, level + 1, fh)
        else:
            if intent:
                for num in range(level):
                    print >> fh, "\t"
            print >> fh, sub_list


man = []
other = []
try:
    data = open('sketch.txt')
    for line in data:
        try:
            (actor, msg) = line.split(":", 1)
            msg = msg.strip()
            if actor == 'Man':
                man.append(msg)
            elif actor == 'Other Man':
                other.append(msg)
        except ValueError:
            pass
    with open('man_file.txt', 'w') as man_file, open('other_file.txt', 'w') as other_file:
        print_list(man, True, 1, fh=man_file)
        print_list(other, fh=other_file)
except IOError as error:
    print('File does no  exist! error : \n' + str(error))

try:
    with open('with.txt', 'w') as with_data:
        print >> with_data, "This is with to open file"
except IOError as error:
    print 'File error : ' + str(error)

out = open('data.out', 'w+')
out.write("Test output....")
out.close()

# help(''.split(':'))

