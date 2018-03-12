import numpy as yummy_yummy_numpy
import csv
import FlightAwareScraper
import unidecode
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
            if i != 1:
                path_list.append(Path(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],
                                      row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27],
                                      row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36],
                                      row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45]))
            i += 1
    return yummy_yummy_numpy.array(path_list)

def import_flights(file, max_flights=0):
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


def get_airports(file, new_file, max_flights=0):
    airport_list = []
    with open(file, 'rb') as flightfile:
        flightreader = csv.reader(flightfile, delimiter=',')
        i = 1
        callsigns = []
        for row in flightreader:
            if i >= max_flights != 0:
                break
            if row[8] not in callsigns:
                callsigns.append(row[8])
                airport_list.append(FlightAwareScraper.get_airports(row[8]))
            i += 1
    with open(new_file, 'wb') as airportfile:
        airportwriter = csv.writer(airportfile, delimiter=',')
        for entry in airport_list:
            airportwriter.writerow(entry)


#For creating a new flight history file
def get_flight_history(callsign_file, new_file, max_flights=0):
    webdriver = FlightAwareScraper.login()

    with open(new_file, 'wb') as historyfile:
        historywriter = csv.writer(historyfile, delimiter=',')
        historywriter.writerow(['callsign', 'date', 'aircraft', 'origin_long', 'origin',
                                        'destination_long', 'destination', 'departure_time',
                                        'departure_time_zone', 'arrival_time', 'arrival_time_zone'])
        with open(callsign_file, 'rb') as flightfile:
            i = 0
            for callsign in flightfile.read().split(','):
                if i >= max_flights != 0:
                    break
                try:
                    flight_history = FlightAwareScraper.get_flight_history(callsign, webdriver)
                    for datapoint in flight_history:
                        historywriter.writerow(datapoint)
                except Exception:
                    print "Error found at line" + str(i)

                i += 1
                if i % 25 == 0:
                    print i


get_flight_history('DATA/callsigns2.csv', 'DATA/flight_history_2-20-18_PART_2.csv')
