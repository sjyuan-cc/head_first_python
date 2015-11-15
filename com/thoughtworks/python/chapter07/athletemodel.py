import pickle
from athlete_list import AthleteList


def read_dic_data(file_name):
    try:
        with open(file_name) as file_in:
            data = file_in.readline().strip().split(',')
            return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as error:
        print(str(error))
        return None


def put_to_store(file_list):
    all_athletes = []
    for each_file in file_list:
        ath = read_dic_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athlete.pickel', 'wb') as athlete_file:
            pickle.dump(all_athletes, athlete_file)
    except IOError as error:
        print 'File error,put to store: ' + str(error)
    return all_athletes


def get_from_store():
    all_athletes = []
    try:
        with open('athlete.pickel', 'rb') as athlete_file:
            all_athletes = pickle.load(athlete_file)
    except IOError as error:
        print 'File error, get from store: ' + str(error)
    return all_athletes
