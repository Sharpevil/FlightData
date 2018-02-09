import csv
from LiveFlights.Path import Path
from LiveFlights.PathEntry import PathEntry

def import_paths_from_flights(file, max_paths=0):
    with open(file, 'rb') as pathfile:
        pathreader = csv.reader(pathfile, delimiter=',')
        i = 1
        path_list = []
        path_entry_list = []
        callsign = ""
        for row in pathreader:
            if i >= max_paths != 0:
                break
            else:
                if row[8] != callsign and i > 1:
                    path_list.append(Path(path_entry_list, callsign))
                    path_entry_list = []
                    callsign = row[8]
                path_entry_list.append(PathEntry(row[1], row[2], row[3]))
                print i
                i = i+1
        path_list.append(Path(path_entry_list, callsign))

        #TODO: Normalize multiple paths for single callsign

import_paths_from_flights("..\DATA\sorted_2018-01-20-20_32.csv")
