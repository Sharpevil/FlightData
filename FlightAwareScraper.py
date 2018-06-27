# encoding=utf8
import sys
import urllib2
import os
import unidecode
from selenium import webdriver
from selenium import common
import selenium
import datetime
import csv
reload(sys)
sys.setdefaultencoding('utf8')


def login():
    ff = webdriver.Firefox()
    ff.get("https://flightaware.com/account/login")
    username = ff.find_element_by_name("flightaware_username")
    password = ff.find_element_by_name("flightaware_password")
    username.send_keys("MSERESEA")
    password.send_keys("hcraeser")
    ff.find_element_by_class_name("actionButton").click()

    return ff


def get_airport_flights(airport, webdriver):
    webdriver.get('https://flightaware.com/live/airport/' + airport)
    html = webdriver.page_source
    html = html.split('Row_other_')
    flights = []
    for sect in html[1:]:
        sect = sect.split('"')
        flights.append(sect[0])
        print sect[0]
    return flights


def get_origin_and_destination(webdriver):
    origin = "UNKNOWN ERROR"
    destination = "UNKNOWN ERROR"
    try:
        html = webdriver.page_source
        origin = html.split('<meta name="origin" content="')[1].split('"')[0]
        destination = html.split('<meta name="destination" content="')[1].split('"')[0]
    except IndexError:
        print "IndexError, could not get origin/destination"
    return [origin, destination]


def get_flight_points(flight, webdriver):
    print flight
    now = datetime.datetime.now()

    webdriver.get('https://flightaware.com/live/flight/' + flight)
    origin_and_destination = get_origin_and_destination(webdriver)
    try:
        webdriver.find_element_by_link_text("graph").click()
    except:
        print "Graph not found"
        return

    html1 = webdriver.page_source
    html2 = html1
    html1 = html1.split('<tr class="smallrow1">')
    html2 = html2.split('<tr class="smallrow2">')
    datapoints = []

    for sect in html1[1:]:
        datapoint = []
        sect = sect.split('</tr>')[0]
        sect = sect.split('">')
        for subsect in sect:
            if subsect.split("<")[0]:
                datapoint.append(subsect.split("<")[0])
        datapoints.append(datapoint)

    for sect in html2[1:]:
        datapoint = []
        sect = sect.split('</tr>')[0]
        sect = sect.split('">')
        for subsect in sect:
            if subsect.split("<")[0]:
                datapoint.append(subsect.split("<")[0])
        datapoints.append(datapoint)

    final_data = []
    for point in datapoints:
        print point
        try:
            final_data.append([str(now.month) + str(now.day)+ flight, point[4], point[6], point[7], point[11], point[13],
                           point[14].split("&")[0], origin_and_destination[0], origin_and_destination[1]])
        except IndexError:
            print "IndexError! Point not logged!"

    return final_data


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


def gather_points(pointfile, airportfile):

    #First, import the airport codes from the file.
    airport_list = []
    with open(airportfile, 'rb') as airports:
        airportreader = csv.reader(airports, delimiter=',')
        i = 0
        for row in airportreader:
            if i > 0:
                airport_list.append(row[1])
            i += 1

    #Then, for each airport, build a list of recent flights to and from it, and write the points for each flight.
    wd = login()
    with open(pointfile, 'wb') as points:
        pointwriter = csv.writer(points, delimiter=',')
        for airport in airport_list:
            print airport
            flights = get_airport_flights(airport, wd)
            for flight in flights:
                flight_points = get_flight_points(flight, wd)
                try:
                    for row in flight_points:
                        pointwriter.writerow(row)
                except TypeError:
                    print "No points"


gather_points('DATA/GatheredPoints.csv', 'DATA/AirportCodeLocationLookupClean.csv')

