import urllib2
import os
import unidecode
from selenium import webdriver


def login():
    ff = webdriver.Firefox()
    ff.get("https://flightaware.com/account/login")
    username = ff.find_element_by_name("flightaware_username")
    password = ff.find_element_by_name("flightaware_password")
    username.send_keys("MSERESEA")
    password.send_keys("hcraeser")
    ff.find_element_by_class_name("actionButton").click()

    return ff


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

    return [callsign, origin, destination]


def get_flight_history(callsign, webdriver, num_entries=500):
    webdriver.get('https://flightaware.com/live/flight/' + str(callsign) + '/history/' + str(num_entries))
    html = webdriver.page_source
    html = html.split('<td class="nowrap">')

    vital_lines = [1, 3, 5, 7, 10, 12, 12, 15, 16, 18, 19]
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
                flight.append(unidecode.unidecode(info[i].split('&nbsp')[0]))
            except IndexError:
                flight.append("ERROR")
        history.append(flight)
    return history
