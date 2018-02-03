import nvector as nv

frame = nv.FrameE(a=6371e3, f=0)

# Check to see if a flight entry falls on a given path, within leniency km of distance
# returns the distance from the path divided by leniency. Thus, a match will always be between 0 and 1.
def point_on_path(flight_entry, path, leniency):
    smallest_dist = 1000000
    for path_section in path.path_sections:
        path_point_a = frame.GeoPoint(float(path_section.wpt1_wgs_dlat),
                                      float(path_section.wpt1_wgs_dlong), degrees=True)
        path_point_b = frame.GeoPoint(float(path_section.wpt2_wgs_dlat),
                                      float(path_section.wpt2_wgs_dlong), degrees=True)
        flight_point = frame.GeoPoint(float(flight_entry.latitude),
                                      float(flight_entry.longitude), degrees=True)
        geo_path = nv.GeoPath(path_point_a, path_point_b)

        xt_dist = abs(geo_path.cross_track_distance(flight_point, method='greatcircle').ravel())
        smallest_dist = min(smallest_dist, xt_dist)

    return float(smallest_dist) / float(leniency)

# Check to see if a flight follows a given path, within leniency km of distance.
# Determines tendency to stay on flight path by averaging the distance of each point from the path.
# Returns between 0 and 1 on a match. Higher numbers
def flight_on_path(flight, path, leniency):
    deviation = 0
    for flight_entry in flight.flightEntries:
        deviation += point_on_path(flight_entry, path, leniency) / flight.flightEntries.size
    return deviation

# Check to see if a flight's heading matches that of a path, within leniency degrees
def check_heading(flight, path, leniency):
    return

# Check to see if a flight's altitude falls within the altitude of a path, potentially allowing it to be leniency units
# outside.
def check_altitude(flight, path, leniency=0):
    return