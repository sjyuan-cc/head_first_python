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


sarah = read_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are " + str(sorted(set([sanitize(each) for each in sarah]))[0:3]))

print('\n========user dictionary=======')
sarah_data = dict()
sarah = read_data('sarah2.txt')
sarah_data['name'] = sarah.pop(0)
sarah_data['dob'] = sarah.pop(0)
sarah_data['times'] = sarah
print(sarah_data['name'] + "'s fastest times are " + str(
    sorted(set([sanitize(each) for each in sarah_data['times']]))[0:3]))

print('\n========encapsulate=======')


def read_dic_data(file_name):
    try:
        with open(file_name) as file_in:
            data = file_in.readline().strip().split(',')
            return {
                'name': data.pop(0),
                'dob': data.pop(0),
                'times': sorted(set([sanitize(time) for time in data]))[0:3],
            }
    except IOError as error:
        print(str(error))
        return None


print(read_dic_data('sarah2.txt'))

dics = {'1': '11', '2': '22'}
for dic in dics:
    print(dic + '-->', end='')
    print(dics[dic])


def test(arg1, arg2, arg3=None):
    print('arg1->'+arg1)
    print('arg2->'+arg2)
    print('arg3->'+str(arg3))


args = ['22', '33']
kwargs = {'arg2': '22', 'arg3': 33}

print(test('00', *args))
print(test('00', **kwargs))
