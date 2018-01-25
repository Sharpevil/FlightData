class Flight:

    def __init__(self, lat, long, alt, heading, speed, histogram):
        self.lat = lat
        self.long = long
        self.alt = alt
        self.heading = heading
        self.speed = speed
        self.histogram = histogram

    def to_string(self):
        return "(" + str(self.lat) + ", " + str(self.long) + ") Alt: " + str(self.alt) + " Dir: " + str(self.heading)


