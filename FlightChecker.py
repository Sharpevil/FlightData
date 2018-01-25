from Flight import Flight
import nvector as nv


frame = nv.FrameE(a=6371e3, f=0)


def create_flight(flight):
    split = flight.split(",")
    return Flight(split[0], split[1], split[2], split[3], split[4], split[5])


#Check to see if a flight is on a given path, within leniency units of distance
def on_path(flight, path, leniency):

    return


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