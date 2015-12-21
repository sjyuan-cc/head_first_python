def read_data(file_name):
    try:
        with open(file_name) as file_in:
            return file_in.readline().strip().split(',')
    except IOError as error:
        print(str(error))
        return None


def sanitize(time):
    if ':' in time:
        splitter = ':'
    elif '-' in time:
        splitter = '-'
    else:
        return time
    (minute, sec) = time.split(splitter)
    return minute + '.' + sec


james = read_data('james.txt')
julie = read_data('julie.txt')
mikey = read_data('mikey.txt')
sarah = read_data('sarah.txt')
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []
for each in james:
    clean_james.append(sanitize(each))
for each in james:
    clean_julie.append(sanitize(each))
for each in james:
    clean_mikey.append(sanitize(each))
for each in james:
    clean_sarah.append(sanitize(each))
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

clean_james = [sanitize(each) for each in james]
clean_julie = [sanitize(each) for each in julie]
clean_mikey = [sanitize(each) for each in mikey]
clean_sarah = [sanitize(each) for each in sarah]
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

print('======manually remove duplicate======')
unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []
for each in clean_james:
    if each not in unique_james:
        unique_james.append(each)

for each in clean_julie:
    if each not in unique_julie:
        unique_julie.append(each)

for each in clean_mikey:
    if each not in unique_mikey:
        unique_mikey.append(each)

for each in clean_sarah:
    if each not in unique_sarah:
        unique_sarah.append(each)
print(sorted(unique_james)[0:3])
print(sorted(unique_julie)[0:3])
print(sorted(unique_mikey)[0:3])
print(sorted(unique_sarah)[0:3])

print('===========set============')
print(sorted(set(sanitize(each) for each in james))[0:3])
print(sorted(set(sanitize(each) for each in julie))[0:3])
print(sorted(set(sanitize(each) for each in mikey))[0:3])
print(sorted(set(sanitize(each) for each in sarah))[0:3])

print([index + 5 for index in range(10)])

s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
print 'adam' in s
print 'bart' in s


def average(*args):
    sum = 0
    for a in args:
        sum += a

    return sum / float(len(args))


print average(1, 2)
print average(1, 2, 2, 3, 4)
