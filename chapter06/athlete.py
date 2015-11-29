def sanitize(time):
    if ':' in time:
        splitter = ':'
    elif '-' in time:
        splitter = '-'
    else:
        return time
    (minute, sec) = time.split(splitter)
    return minute + '.' + sec


class Athlete:
    def __init__(self, name, dob=None, times=[]):
        self.name = name
        self.dob = dob
        self.times = times

    def top3(self):
        return sorted(set(sanitize(each) for each in self.times))[0:3]

    def add_time(self, time=None):
        self.times.append(time)

    def add_times(self, times=[]):
        self.times.extend(times)


def read_dic_data(file_name):
    try:
        with open(file_name) as file_in:
            data = file_in.readline().strip().split(',')
            return Athlete(data.pop(0), data.pop(0), data)
    except IOError as error:
        print(str(error))
        return None


print(read_dic_data('sarah2.txt').top3())
