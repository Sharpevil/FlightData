import csv
import requests

url = "http://api.geonames.org/timezoneJSON?lat=<LAT>&lng=<LONG>&username=armstr27"

def add_adjusted_epochs(filename, updated):
    with open(filename, 'rb') as original_file:
        filereader = csv.reader(original_file, delimiter=',')
        with open(updated, 'wb') as updated_file:
            filewriter = csv.writer(updated_file, delimiter=',')
            header = True
            for row in filereader:
                if not header:
                    a = 1
                else:
                    header_row = []
                    for column in row:
                        header_row.append(column)
                    header_row.append("origin_epoch_time")
                    header_row.append("dest_epoch_time")
                    filewriter.writerow(header_row)
                    header = False

def add_offsets_to_file(filename, updated):
    lines = 0
    timezones = {'EST': -5}
    with open(filename, 'rb') as original_file:
        filereader = csv.reader(original_file, delimiter=',')
        with open(updated, 'wb') as updated_file:
            filewriter = csv.writer(updated_file, delimiter=',')
            header = True
            for row in filereader:
                if not header:
                    if row[8] not in timezones:
                        origin_utc_offset = get_utc_offset(row[11], row[12], row[8])
                        timezones[row[8]] = origin_utc_offset
                    if row[10] not in timezones:
                        dest_utc_offset = get_utc_offset(row[13], row[14], row[10])
                        timezones[row[10]] = dest_utc_offset
                    new_row = []
                    for column in row:
                        new_row.append(column)
                    new_row.append(timezones[row[8]])
                    new_row.append(timezones[row[10]])
                    filewriter.writerow(new_row)
                    lines += 1
                    if lines % 100 == 0:
                        fun_loading_bar(lines, 637800)
                else:
                    header_row = []
                    for column in row:
                        header_row.append(column)
                    header_row.append("origin_utc_offset")
                    header_row.append("dest_utc_offset")
                    filewriter.writerow(header_row)
                    header = False


def get_utc_offset(lat, long, tz):
    utc_offset = "N/A"
    request = requests.get(url.replace("<LAT>", str(lat)).replace("<LONG>", str(long)))
    if tz != "Diverted":
        if "DT" in tz:
            try:
                utc_offset = request.json()["dstOffset"]
            except:
                utc_offset = "ERROR"
        else:
            try:
                utc_offset = request.json()["gmtOffset"]
            except:
                utc_offset = "ERROR"
    return utc_offset


def fun_loading_bar(curr_line, total_lines):
    progress = (float(curr_line) / float(total_lines)) * 20
    loading_bar = "["
    for i in range(1, 20):
        if i <= progress:
            loading_bar += "#"
        else:
            loading_bar += "-"
    loading_bar += "] " + str(curr_line) + "/" + str(total_lines)
    print loading_bar



