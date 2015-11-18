import pickle
from chapter07.athlete_list import AthleteList


def read_dic_data(file_name):
    try:
        with open(file_name) as file_in:
            data = file_in.readline().strip().split(',')
            return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as error:
        print(str(error))
        return None


def put_to_store(files):
    all_athletes = {}
    for each_file in files:
        ath = read_dic_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athlete.pickle', 'wb') as athlete_file:
            pickle.dump(all_athletes, athlete_file)
    except IOError as error:
        print
        'File error,put to store: ' + str(error)
    return all_athletes


def get_from_store():
    all_athletes = []
    try:
        with open('athlete.pickle', 'rb') as athlete_file:
            all_athletes = pickle.load(athlete_file)
    except IOError as error:
        print('File error, get from store: ' + str(error))
    return all_athletes


file_list = ['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt']
saved_data = put_to_store(file_list)
print(saved_data)

for every in saved_data:
    print(saved_data[every].name + ',' + saved_data[every].dob)

loaded_data = get_from_store()
for every in loaded_data:
    print(loaded_data[every].name + ',' + loaded_data[every].dob)
