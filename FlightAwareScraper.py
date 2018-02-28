import urllib2
import os

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

def get_flight_history(callsign):
    response = urllib2.urlopen('https://flightaware.com/live/flight/' + callsign + '/history')
    html = response.read()
    html = html.split('<td class="nowrap" >')

    vital_lines = [0, 1, 2, 4, 6, 8, 10, 11, 12, 13]
    history = []

    for line in html[1:len(html) - 1]:
        info = ""
        flight = [callsign]
        line = line.split('>')
        for fragment in line:
            info += fragment.split('<')[0].strip() + "\n"
        info = os.linesep.join([s for s in info.splitlines() if s]).split('\r\n')
        for i in vital_lines:
            try:
                flight.append(info[i])
            except IndexError:
                flight.append("ERROR")
        history.append(flight)
    return history