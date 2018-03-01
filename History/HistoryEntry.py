from dateutil import parser
import datetime

monthMap = {}

map["Feb"] = 2
map["Mar"] = 3


class HistoryEntry:

    def __init__(self, date, origin, destination, departureTime,departure_time_zone, ArrivalTime, arrival_time_zone):
        self.origin = origin
        self.destination = destination


    
now = parser.parse("Sat Oct 11 17:13:46 UTC 2003")

import time
dt = datetime.datetime
year = 2003
month = 10
day = 11
hour = 17
minute = 13
second = 46
print time.mktime((year, month, day, hour, minute, second, 0, 0, 0))
print time.time()
print time.mktime((2018, 3, 1, 11, 5, 0, 0, 0, 0))
print time.mktime((2018, HistoryEntry.monthMap.get("Mar"), 1, 11, 5, 0, 0, -500, -1))*1000

print time.time()