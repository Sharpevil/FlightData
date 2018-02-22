import urllib2

#TODO - get the departure time - the arrival time - and the date
#TODO - as well as what we're already getting.

#TODO - after we get this info, check the time on an aircraft to
#TODO - see which one it falls within in order to check which origin
#TODO - or destination to use.
def get_airports(callsign):
    response = urllib2.urlopen('https://flightaware.com/live/flight/' + callsign + '/history')
    html = response.read()

    origin = "N/A"
    destination = "N/A"

    #should store the departure time
    departure = "N/A"
    #should store the arrival time
    arrival = "N/A"
    #should store the start date of a flight(maybe not needed if we get the above 2 in unix time
    startDate = "N/A"

    #might need to redo some of this
    #destination and origin seem to come after "url">
    origin_iata = html.find("setTargeting('origin_IATA', '")
    destination_iata = html.find(".setTargeting('destination_IATA', '")
    if origin_iata != -1:
        origin = html[origin_iata + 29:origin_iata+32]
    if destination_iata != -1:
        destination = html[destination_iata+35:destination_iata+38]


    return [callsign,origin,destination]
