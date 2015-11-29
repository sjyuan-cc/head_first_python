import glob
import pickle
from datetime import timedelta, datetime

import re

from chapter07.athlete_list import AthleteList
from chapter09.tables_creatioin import *


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as io_err:
        print('File error (get_coach_data): ' + str(io_err))
        return None


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as io_err:
        print('File error (put_and_store): ' + str(io_err))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as io_err:
        print('File error (get_from_store): ' + str(io_err))
    return all_athletes


data_files = glob.glob('data/*.txt')
athletes = put_to_store(data_files)
create_tables()
connection = create_connection('test.sqlite3')
cursor = connection.cursor()
for athlete in athletes:
    name = athletes[athlete].name
    dob = athletes[athlete].dob
    cursor.execute('insert into athlete(name,dob) values(?,?)', (name, dob))
    connection.commit()
    cursor.execute('select id from athlete where name=? and dob=?', (name, dob))
    the_current_id = cursor.fetchone()[0]
    times = athletes[athlete].times
    for time in times:
        cursor.execute('insert into timing_data (athlete_id,value) values(?,?)', (the_current_id, time))
        connection.commit()

connection.close()

now = datetime.strptime('2015-11-11', '%Y-%m-%d')
print(now)
now1 = now + timedelta(0.5)
print(now1)
print(now1 > now)

import re

result = re.split(' |,', 'name pass,age')
print(result)
