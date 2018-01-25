import numpy as yummy_yummy_numpy
import csv
from Path import Path
from Flight import Flight


def import_paths(file, max_paths=0):
    with open(file, 'rb') as pathfile:
        pathreader = csv.reader(pathfile, delimiter='\t')
        i = 1
        path_list = []
        for row in pathreader:
            if i >= max_paths != 0:
                break
            path_list.append(Path(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                  row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],
                                  row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27],
                                  row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36],
                                  row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45]))
            i += 1
    return yummy_yummy_numpy.array(path_list)

def import_flights(file, max_flights):
    with open(file, 'rb') as flightfile:
        flightreader = csv.reader(flightfile, delimiter=',')
        i = 1
        flight_list = []
        for row in flightreader:
            if i >= max_flights != 0:
                break
            flight_list.append(Flight(row[0], row[1], row[2], row[3], row[4], row[5]))
            i += 1
    return yummy_yummy_numpy.array(flight_list)

