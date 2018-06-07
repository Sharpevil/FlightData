import os
from HistoryEntry import HistoryEntry

def create_full_flight_history_file(flight_history, airport_code_lookup, optd_por, out_file):
    flight_history_file = open(flight_history, 'r')
    airport_code_lookup_file = open(airport_code_lookup, 'r')
    optd_por_file = open(optd_por, 'r')
    out_file = open(out_file, 'w')

    iata_to_lat_long_map = {}

    for line in airport_code_lookup_file:
        values = line.split(',')
        iata = values[1]
        latitude = values[3]
        longitude = values[4]

        iata_to_lat_long_map[iata] = latitude + ',' + longitude[:len(longitude) - 1]
    airport_code_lookup_file.close()

    icao_to_iata_map = {}

    for line in optd_por_file:
        values = line.split('^')
        iata = values[0]
        icao = values[1]
        if icao != "":
            icao_to_iata_map[icao] = iata
    optd_por_file.close()

    header = flight_history_file.next()
    header = header[:len(header) - 1]
    out_file.write(header + ",origin_latitude,origin_longitude,destination_latitude,destination_longitude\n")
    lineNum = 0
    for line in flight_history_file:
        lineNum += 1
        values = line.split(',')

        callsign = values[0]
        date = values[1]
        aircraft = values[2]
        origin_long = values[3]
        #ICAO format
        origin = values[4]
        destination_long = values[5]
        #ICAO format
        destination = values[6]
        departure_time = values[8]
        departure_time_zone = values[9]
        arrival_time = values[10]
        try:
            arrival_time_zone = values[11]
            arrival_time_zone = arrival_time_zone[:len(arrival_time_zone) - 1]
        except Exception:
            print "error on line Num" + str(lineNum)
            print line
            continue
        if(lineNum%10000 == 0):
            print "Finished " + str(lineNum)

        nextLine = callsign + ',' + date + ',' + aircraft + ',' + origin_long + ',' + origin + ',' + destination_long + ',' + destination + ',' + departure_time + ',' + departure_time_zone + ',' + arrival_time + ',' + arrival_time_zone

        if origin in icao_to_iata_map.keys() and destination in icao_to_iata_map.keys():
            if icao_to_iata_map[origin] in iata_to_lat_long_map.keys() and icao_to_iata_map[destination] in iata_to_lat_long_map.keys():
                nextLine += ',' + iata_to_lat_long_map[icao_to_iata_map[origin]] + ',' + iata_to_lat_long_map[icao_to_iata_map[destination]]
            else:
                continue
        else:
            continue
        out_file.write(nextLine + '\n')

def getHistory(historyPath):
    historyFile = open(historyPath)
    for line in historyFile:
        end = 1
        #TODO create a map of call signs to sets of time with origin and destination associated with the time


def create_Orig_Dest_File_With_Time(origin_destination_file, new_origin_destination_file):
    in_file = open(origin_destination_file, 'r')
    out_file = open(new_origin_destination_file, 'w')
    header = in_file.readline()
    header = header[:len(header) - 1]
    out_file.write(header + ',' + "origin_time_Unix" + ',' + "destination_time_Unix\n")
    lineNum = 0
    for line in in_file:
        lineNum += 1
        if lineNum%1 == 0:
            print "Finished : " + str(lineNum)

        if line == "callsign,date,aircraft,origin_long,origin,destination_long,destination,departure_time,departure_time_zone,arrival_time,arrival_time_zone,origin_latitude,origin_longitude,destination_latitude,destination_longitude\n":
            continue
        #get rid of new line\
        line = line[:len(line) -1]
        values = line.split(',')
        arrival_time_zone = values[10]
        #Throw out diverted flights.
        if(arrival_time_zone == "Diverted" or arrival_time_zone == "?"):
            continue
        date = values[1]
        destination = values[6]
        origin = values[4]
        destination_time = values[9]#also known as arrival time
        origin_time = values[7]#also known as departure time
        destination_lat = float(values[13])
        destination_long = float(values[14])
        origin_lat = float(values[11])
        origin_long = float(values[12])
        history = HistoryEntry(date, origin, destination, destination_time, destination_lat, destination_long, origin_time, origin_lat, origin_long)
        out_file.write(line + ',' + str(history.origin_departure_time) + ','+ str(history.destination_arrival_time) + '\n')

def fixDates(oldFile, newFile):
    out_file = open(newFile, 'w')
    old_history = open(oldFile, 'r')
    #remove header
    old_history.readline()
    for line in old_history:
        values = line.split(',')
        print values[1]
        date = values[1]
        if ('-' in date):
            date = date.split('-')
        elif ('/' in date):
            date = date.split('/')

        if (len(date[0]) == 2):
            newDate = date[0] + '-' + date[1] + '-' + date[2]
        else:
            newDate = date[2] + '-' + date[1] + '-' + date[0]
        values[1] = newDate
        out_file.write(','.join(values))

os.chdir(r"C:\Users\Resea\Downloads\flights")
create_Orig_Dest_File_With_Time("Better_Best_History.csv", "Best_History_With_Unix_Times.csv")
