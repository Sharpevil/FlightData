import os
def getHistory(historyPath = r"C:\Users\Resea\Downloads\flights\newHistory.csv"):
    historyFile = open(historyPath)
    for line in historyFile:
        end = 1
        #TODO create a map of call signs to sets of time with origin and destination associated with the time


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

os.chdir(r"C:\Users\Resea\Downloads\flights")
create_full_flight_history_file("flight_history.csv", "AirportCodeLocationLookupClean.csv", "optd_por_public.csv", "Best_History.csv")