from dateutil import parser
import datetime
import time
from timezonefinder import TimezoneFinder
import pytz, datetime
import calendar

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

    #currently assumes no leap years
    #index + 1 = month num
    daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

    def __init__(self, date, origin, destination, destination_time, destination_lat, destination_long, origin_time, origin_lat, origin_long):
        self.origin = origin
        self.destination = destination

        dateValues = date.split('-')
        origin_day = int(dateValues[0])
        if(len(dateValues[1]) == 3):
            origin_month = HistoryEntry.monthMap.get(dateValues[1])
        else:
            origin_month = int(dateValues[1])
        if(len(dateValues[2]) == 2):
            origin_year = int("20" + dateValues[2])
        else:
            origin_year = int(dateValues[2])

        origin_AM_or_PM = origin_time[len(origin_time) - 2:]
        origin_time = origin_time[:5]
        origin_hour = int(origin_time[:2])
        origin_minute = int(origin_time[3:6])
        if(origin_AM_or_PM == "PM"):
            if(origin_hour < 12):
                origin_hour += 12
        else:
            if(origin_hour == 12):
                origin_hour = 0

        destination_AM_or_PM = destination_time[len(destination_time) - 2:]
        destination_time = destination_time[:5]
        #TODO - if the path is diverted, we can not use anything regarding destination.
        destination_hour = int(destination_time[:2])
        destination_minute = int(destination_time[3:6])
        if(destination_AM_or_PM == "PM"):
            if(destination_hour < 12):
                destination_hour += 12
        else:
            if(destination_hour == 12):
                destination_hour = 0

        if(destination_hour < origin_hour):
            destination_day = origin_day + 1
        else:
            destination_day = origin_day
        destination_year = origin_year
        destination_month = origin_month

        tf = TimezoneFinder()
        origin_time_zone = tf.timezone_at(lng = origin_long, lat = origin_lat)
        destination_time_zone = tf.timezone_at(lng = destination_long, lat = destination_lat)

        # hour offset is in the format +/- XXYY where XX:YY is the amount of offset, and +/- means positive or negative
        # datetiem takes attributes in the order year, month, day, hour, minute, second, microsecond, and tzinfo.
        origin_time_offset = pytz.timezone(origin_time_zone).localize(datetime.datetime(
            origin_year,
            origin_month,
            origin_day,
            origin_hour,
            origin_minute
        )).strftime('%z')
        if(destination_day > HistoryEntry.daysInMonth[destination_month -1]):
            destination_month += 1
            if(destination_month > 12):
                destination_month = 1
            destination_day = 1

        destination_time_offset = pytz.timezone(destination_time_zone).localize(datetime.datetime(destination_year, destination_month, destination_day, destination_hour, destination_minute)).strftime('%z')

        if(origin_time_offset[0] == '-'):
            origin_hour_offset = int(origin_time_offset[0:3])
        elif(origin_time_offset[0] == '+'):
            origin_hour_offset = int(origin_time_offset[0:3])
        else:
            origin_hour_offset = int(origin_time_offset[0:2])

        if(origin_time_offset[0] == '-'):
            origin_minute_offset = int(origin_time_offset[3:5])*(-1)
        elif(origin_time_offset[0] == '+'):
            origin_minute_offset = int(origin_time_offset[3:5])
        else:
            origin_minute_offset = int(origin_time_offset[2:4])


        if(destination_time_offset[0] == '-'):
            destination_hour_offset = int(destination_time_offset[0:3])
        elif(origin_time_offset[0] == '+'):
            destination_hour_offset = int(destination_time_offset[0:3])
        else:
            destination_hour_offset = int(destination_time_offset[0:2])

        if(destination_time_offset[0] == '-'):
            destination_minute_offset = int(destination_time_offset[3:5])*(-1)
        elif(origin_time_offset[0] == '+'):
            destination_minute_offset = int(destination_time_offset[3:5])
        else:
            destination_minute_offset = int(destination_time_offset[2:4])

        #TODO - get the Epoch time based on date/time, and then add offset

        origin_departure_time = calendar.timegm((origin_year, origin_month, origin_day, origin_hour, origin_minute, 0, 0, 0, 0)) * 1000 #(change it from seconds to milliseconds
        origin_departure_time += (origin_minute_offset * 60 * 1000)
        origin_departure_time += (origin_hour_offset * 60 * 60 * 1000)
        self.origin_departure_time = origin_departure_time

        destination_arrival_time = calendar.timegm((destination_year, destination_month, destination_day, destination_hour, destination_minute, 0, 0, 0, 0)) * 1000
        destination_arrival_time += (destination_minute_offset * 60 * 1000)
        destination_arrival_time += (destination_hour_offset * 60 * 60 * 1000)
        self.destination_arrival_time = destination_arrival_time





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

# tf = TimezoneFinder()
#
# latitude = 26.53611111
# longitude = -81.75527778
#
# timezone = tf.timezone_at(lng = longitude, lat = latitude)
# #hour offset is in the format +/- XXYY where XX:YY is the amount of offset, and +/- means positive or negative
# #datetiem takes attributes in the order year, month, day, hour, minute, second, microsecond, and tzinfo.
# origin_time_zone = tf.timezone_at(lng= -0.076132, lat=51.508530)#GMT
# origin_time_zone = tf.timezone_at(lng =-74.742935, lat =0.217052 )
#
# hour_offset = pytz.timezone(origin_time_zone).localize(datetime.datetime(2018,2,11)).strftime('%z')
# print int(hour_offset)

# history_entry = HistoryEntry("3-Mar-18", "Here", )
#
# print time.mktime(time.localtime())
# print calendar.timegm(time.localtime())