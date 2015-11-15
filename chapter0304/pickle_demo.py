import pickle

with open('save_data.txt', 'wb') as save_file:
    pickle.dump([1, 2, 'Three'], save_file)

with open('save_data.txt', 'rb') as load_file:
    load_data = pickle.load(load_file)
print load_data
