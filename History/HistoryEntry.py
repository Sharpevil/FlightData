from dateutil import parser
import datetime
import time
from timezonefinder import TimezoneFinder
import pytz, datetime


monthMap = {}

monthMap["Feb"] = 2
monthMap["Mar"] = 3


class HistoryEntry:
    monthMap = {}
    monthMap["Jan"] = 1
    monthMap["Feb"] = 2
    monthMap["Mar"] = 3
    monthMap["Apr"] = 4
    monthMap["May"] = 5
    monthMap["Jun"] = 6
    monthMap["Jul"] = 7
    monthMap["Aug"] = 8
    monthMap["Sep"] = 9
    monthMap["Oct"] = 10
    monthMap["Nov"] = 11
    monthMap["Dec"] = 12


    def __init__(self, date, origin, destination, arrival_time, arrival_lat, arrival_long, departure_time, departure_lat, departure_long):
        self.origin = origin
        self.destination = destination

        dateValues = date.split('-')
        day = int(dateValues[0])
        month = monthMap.get(dateValues[1])
        year = int("20" + dateValues[2])

        departure_AM_or_PM = departure_time[len(departure_time) - 2:]
        departure_time = departure_time[:5]
        departure_hour = int(departure_time[:2])
        departure_minute = int(departure_time[3:6])
        if(departure_AM_or_PM == "PM"):
            departure_hour += 12

        arrival_AM_or_PM = arrival_time[len(arrival_time) - 2:]
        arrival_time = arrival_time[:5]
        arrival_hour = int(arrival_time[:2])
        arrival_minute = int(arrival_time[3:6])
        print arrival_AM_or_PM
        if(arrival_AM_or_PM == "PM"):
            arrival_hour += 12

        print arrival_hour
        print departure_hour




# historyEntry = HistoryEntry("1-Mar-18", "KRSW", "KBOS", "11:20AM", "EST", "02:06PM", "EST")
#
#
#
#
# dt = datetime.datetime
# year = 2003
# month = 10
# day = 11
# hour = 17
# minute = 13
# second = 46
# print time.mktime((year, month, day, hour, minute, second, 0, 0, 0))
# print time.time()
# print time.mktime((2018, 3, 2, 11, 5, 0, 0, 0, 0))
# print time.mktime((2018, HistoryEntry.monthMap.get("Mar"), 2, 11, 5, 0, 0, -500, -1))*1000
#
#
# print time.timezone
#
# print len(HistoryEntry.monthMap)

tf = TimezoneFinder()

latitude = 26.53611111
longitude = -81.75527778

timezone = tf.timezone_at(lng = longitude, lat = latitude)
#hour offset is in the format +/- XXYY where XX:YY is the amount of offset, and +/- means positive or negative
#datetiem takes attributes in the order year, month, day, hour, minute, second, microsecond, and tzinfo.
hour_offset = pytz.timezone(timezone).localize(datetime.datetime(2018,3,11, 3000)).strftime('%z')
print hour_offset