import urllib2


def get_airports(callsign):
    response = urllib2.urlopen('https://flightaware.com/live/flight/' + callsign)
    html = response.read()

    origin = "N/A"
    destination = "N/A"

    origin_iata = html.find("setTargeting('origin_IATA', '")
    destination_iata = html.find(".setTargeting('destination_IATA', '")
    if origin_iata != -1:
        origin = html[origin_iata + 29:origin_iata+32]
    if destination_iata != -1:
        destination = html[destination_iata+35:destination_iata+38]


    return [callsign,origin,destination]
