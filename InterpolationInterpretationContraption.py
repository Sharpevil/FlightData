import numpy as np
import csv
import pickle

def interpolation_to_csv(datafile, csvfile):
    interpolations = pickle.load(open(datafile))

    with open(csvfile, 'wb') as outfile:
        writer = csv.writer(outfile, delimiter='|')
        for entry in interpolations['interpol']:
            row = []
            gap_size = entry['final time'] / 100
            time_range = np.arange(0, entry['final time'], gap_size)
            for time in time_range:
                row.append(str(time) + ',' + str(entry['lat'](time)) + ',' +
                           str(entry['long'](time)) + ',' + str(entry['alt'](time)))
            writer.writerow(row)

def data_to_csv(datafile, csvfile):
    lists = pickle.load(open(datafile))

    with open(csvfile, 'wb') as outfile:
        writer = csv.writer(outfile, delimiter='|')
        for i in range(0, len(lists[0])):
            row = []
            for j in range(0, len(lists[0][i])):
                row.append([lists[0][i][j], lists[1][i][j], lists[2][i][j], lists[3][i][j]])
            writer.writerow(row)

data_to_csv('./DATA/listsBackup.txt', './DATA/listsBackup.csv')