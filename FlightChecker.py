from Flight import Flight

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