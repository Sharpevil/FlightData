from timezonefinder import TimezoneFinder
from datetime import datetime
from pytz import timezone, utc
from pytz.exceptions import UnknownTimeZoneError
import pickle
import csv

tf = TimezoneFinder()
history = './DATA/flight_history.csv'

#When checking flight history airport codes, ensure to check for dual codes split by /, and take whichever has four letters.

def get_airport_time_zones():
    airports = {}
    airports['timezones'] = []
    with open('./DATA/optd_por_public.csv', 'rb') as lookup:
        reader = csv.reader(lookup, delimiter='^')
        for row in reader:
            if row[1] is not '' and row[1] != 'icao_code':
                print row[1] + " : " + row[9] + " : " + row[8]
                airports['timezones'].append({
                    'icao': row[1],
                    'timezone': tf.certain_timezone_at(lng=float(row[9]), lat=float(row[8]))
            })
    return airports

def convert_history_to_UTC(history_file):
    with open(history_file, 'rb') as old_history:
        with open('new_' + history_file, 'wb') as new_history:
            reader = csv.reader(old_history, delimiter=',')
            writer = csv.writer(new_history, delimiter=',')

            for line in reader:
                if not line[11]:
                    writer.writerow(line)
                else:
                    try:
                        origin = line[4]
                        destination = line[6]
                        times = normalize_date_times(line[1], line[8], line[10])
                    finally:
                        return


def normalize_date_times(date, departure, arrival):
    split_date = date.split('- |/ | \\')



airports = pickle.load(open('./DATA/airport_time_zones.txt'))
