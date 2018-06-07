import numpy as np
import csv
import matplotlib.pyplot as plt
import pickle
from scipy import interpolate

def interpolate_flight(epochs, lats, longs, alts):
    times = []
    for time in epochs:
        times.append(time - epochs[0])
    times = np.asarray(times)
    lats = np.asarray(lats)
    longs = np.asarray(longs)
    alts = np.asarray(alts)

    interpolation_lat = interpolate.UnivariateSpline(times, lats)
    interpolation_long = interpolate.UnivariateSpline(times, longs)
    interpolation_alt = interpolate.UnivariateSpline(times, alts)

    return [interpolation_lat, interpolation_long, interpolation_alt]


def get_callsign_lines(callsign, data_folder, files):
    epoch_lists = [[]]
    lat_lists = [[]]
    long_lists = [[]]
    alt_lists = [[]]
    last_epoch = 0
    num_flights = 0

    for flight_file in files:
        print 'Opening a new file. ' + str(num_flights) + ' flights total thus far.'
        with open(data_folder + flight_file, 'rb') as flightfile:
            callsign_found = False
            flightreader = csv.reader(flightfile, delimiter=',')
            for row in flightreader:
                if not callsign_found and row[8] == callsign:
                    last_epoch = int(row[0])
                    callsign_found = True
                if callsign_found:
                    if row[8] == callsign:
                        if abs(int(row[0]) - last_epoch) > 3600000 or int(row[0]) < last_epoch:
                            epoch_lists.append([])
                            lat_lists.append([])
                            long_lists.append([])
                            alt_lists.append([])
                            last_epoch = int(row[0])
                            num_flights += 1
                            print num_flights
                        epoch_lists[num_flights].append(int(row[0]))
                        lat_lists[num_flights].append(float(row[1]))
                        long_lists[num_flights].append(float(row[2]))
                        alt_lists[num_flights].append(float(row[3]))
    return [epoch_lists, lat_lists, long_lists, alt_lists]


data_folder = './DATA/'
files = ['sorted_2018-01-20-20_32_clean.csv', 'sorted_live_2018-01-20-20_32_clean.csv',
         'sorted_live_2018-01-30-13_20_clean.csv', 'sorted_live_2018-02-03-16_46_clean.csv',
         'sorted_live_2018-02-23-13_10.new_clean.csv']

lists = get_callsign_lines('NKS256', data_folder, files)

with open('./DATA/listsBackup.txt', 'w') as outfile:
    pickle.dump(lists, outfile)

# lists = pickle.load(open('./DATA/listsBackup.txt'))

data = {}
data['interpol'] = []

for i in range(0, len(lists[0])):
    if len(lists[0][i]) > 1:
        try:
            print 'NEW FLIGHT:'
            interpolations = interpolate_flight(lists[0][i], lists[1][i], lists[2][i], lists[3][i])
            data['interpol'].append({
                'name': 'NKS256',
                'lat': interpolations[0],
                'long': interpolations[1],
                'alt': interpolations[0],
                'final time': lists[0][i][len(lists[0][i]) - 1] - lists[0][i][0]
            })
        except ValueError:
            print 'VALUE ERROR'
            print lists[0][i]
            print lists[1][i]
            print lists[2][i]
            print lists[3][i]
        except:
            print lists[0][i]
            print lists[1][i]
            print lists[2][i]
            print lists[3][i]

with open('./DATA/testdata.txt', 'w') as outfile:
    pickle.dump(data, outfile)