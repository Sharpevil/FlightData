from Flight import Flight
import nvector as nv


frame = nv.FrameE(a=6371e3, f=0)


def create_flight(flight):
    split = flight.split(",")
    return Flight(split[0], split[1], split[2], split[3], split[4], split[5])


#Check to see if a flight is on a given path, within leniency km of distance
def on_path(flight, path, leniency):
    path_point_a = frame.GeoPoint(float(path.wpt1_wgs_dlat), float(path.wpt1_wgs_dlong), degrees=True)
    path_point_b = frame.GeoPoint(float(path.wpt2_wgs_dlat), float(path.wpt2_wgs_dlong), degrees=True)
    flight_point = frame.GeoPoint(float(flight.lat), float(flight.long), degrees=True)
    geo_path = nv.GeoPath(path_point_a, path_point_b)

    xt_dist = abs(geo_path.cross_track_distance(flight_point, method='greatcircle').ravel())
    global smallest_dist
    if xt_dist < smallest_dist:
        global closest_path
        closest_path = path
        smallest_dist = xt_dist

    return xt_dist < leniency


#Check to see if a flight's heading matches that of a path, within leniency degrees
def check_heading(flight, path, leniency):
    return


#Check to see if a flight's altitude falls within the altitude of a path, potentially allowing it to be leniency units outside.
def check_altitude(flight, path, leniency):
    return


def cross_track_test():
    frame = nv.FrameE(a=6371e3, f=0)
    pointA1 = frame.GeoPoint(0, 0, degrees=True)
    pointA2 = frame.GeoPoint(10, 0, degrees=True)
    pointB = frame.GeoPoint(1, 0.1, degrees=True)
    pathA = nv.GeoPath(pointA1, pointA2)

    s_xt = pathA.cross_track_distance(pointB, method='greatcircle').ravel()
    d_xt = pathA.cross_track_distance(pointB, method='euclidean').ravel()

    val_txt = '{:4.2f} km, {:4.2f} km'.format(s_xt[0]/1000, d_xt[0]/1000)
    print 'Ex10: Cross track distance: s_xt, d_xt = {}'.format(val_txt)

    pointC = pathA.closest_point_on_great_circle(pointB)
    print pathA.on_path(pointC)
    return

import DataImport

paths = DataImport.import_paths("C:\Users\\armstr\Google Drive\ASRC\DAFIF\Airways\ATS.TXT")
flights = DataImport.import_flights("C:\Users\\armstr\Google Drive\ASRC\DAFIF\August8WriteFile.csv")

for i in xrange(10):
    global smallest_dist
    global closest_path
    smallest_dist = 100000
    closest_path = None
    print "Beginning flight " + str(i)
    for path in paths:
        if on_path(flights[i], path, 15):
            print "Flight " + str(i) + " is on path " + str(path.ats_ident)
    print "The closest path is " + str(closest_path.ats_ident) + " at " + str(smallest_dist) + "km"
