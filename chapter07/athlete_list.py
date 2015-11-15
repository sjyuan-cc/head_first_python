def sanitize(time):
    if ':' in time:
        splitter = ':'
    elif '-' in time:
        splitter = '-'
    else:
        return time
    (minute, sec) = time.split(splitter)
    return minute + '.' + sec


class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.times = times
        self.extend(times)

    def top3(self):
        return sorted(set(sanitize(each) for each in self))[0:3]

    @staticmethod
    def read_dic_data(file_name):
        try:
            with open(file_name) as file_in:
                data = file_in.readline().strip().split(',')
                return AthleteList(data.pop(0), data.pop(0), data)
        except IOError as error:
            print(str(error))
            return None

athlete_list = AthleteList.read_dic_data('sarah2.txt')

print athlete_list.top3()
#
# athlete_list.append('1.2')
# print athlete_list.top3()
