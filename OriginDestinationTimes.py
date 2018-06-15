#container class for origin, destination, and their times
#@author Brennan Ringel
class OriginDestinationTimes:
    def __init__(self, origin, origin_long, destination, destination_long, departure_time, arrival_time):
        self.origin = origin
        self.origin_long = origin_long

        self.destination = destination
        self.destination_long = destination_long

        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def getOrigin(self):
        return self.origin, self.origin_long

    def getOriginLong(self):
        return self.origin_long

    def getDestination(self):
        return self.destination

    def getDestinationLong(self):
        return self.destination_long

    def getDepartureTime(self):
        return self.departure_time

    def getArrivalTime(self):
        return self.arrival_time


# Take History Data, and file(s) from ASRC
# historyDataFile is the file of the history data, and live Datas is an array (any list or set data structure should work)
# of all the live data files.
def labelOriginAndDestination(historyDataFile, liveDatas):
    if len(liveDatas) < 1:
        raise Exception("liveDatas should be of size 1 or larger")

    historyFile = open(historyDataFile)

    historyFile.readline()

    # I need a map of call Signs to times/origin/destination

    callSignToOriginDestinationAndTime = {}

    print 'starting history'
    for line in historyFile:
        values = line.split(',')
        callSign = values[0]
        origin_long = values[3]
        origin = values[4]
        destination_long = values[5]
        destination = values[6]
        # TODO test this
        departure_time_unix = values[17]
        arrival_time_unix = values[18]

        exists = callSignToOriginDestinationAndTime.get(callSign)

        if exists == None:
            callSignToOriginDestinationAndTime[callSign] = set()
        callSignToOriginDestinationAndTime[callSign].add(
            OriginDestinationTimes(origin, origin_long, destination, destination_long, departure_time_unix, arrival_time_unix))
        # set.add(OriginDestinationTimes(origin, origin_long, destination, departure_time_unix, arrival_time_unix))
    print 'finished history, starting livedata'
    numOfLines = 0
    for fileName in liveDatas:
        file = open(fileName, 'r')
        print fileName
        newfile = open(fileName + "OriDest.csv", 'w')
        for line in file:
            numOfLines += 1
            if(numOfLines%1000 == 0):
                print numOfLines
            values = line.split(',')
            message_time = values[0]
            call_sign = values[8]
            origDestSet = callSignToOriginDestinationAndTime.get(call_sign)
            if origDestSet is not None:
                for origDest in origDestSet:
                    if message_time >= origDest.getDepartureTime() and message_time <= origDest.getArrivalTime():
                        origin = origDest.getOrigin()
                        origin_long = origDest.getOriginLong()
                        destination = origDest.getDestination()
                        destination_long = origDest.getDestinationLong()
                        if type(origin) is tuple:
                            origin = origin[0]
                        # print type(',')
                        # print type(origin)
                        # print origin
                        # print type(origin_long)
                        # print origin_long
                        # print type(destination)
                        # print type(destination_long)
                        line = line[:len(line)-1] + ',' + origin + ',' + origin_long + ',' + destination + ',' + destination_long + '\n'
                        # we found the origDest object we wanted, no need to continue searching.
                        break
            #write the line to the new file, hopefully it found the right part of the history file, otherwise it is written without an origin and/or destination
            newfile.write(line)


        file.close()

# TODO Go through list of other files, and add in the origin and destination fields based on the time and call sign

history = r'C:\Users\remem\Downloads\flights\newHistoryFile.csv'
liveDatas = [liveDatasStart + r'\live_2018-02-23-13_10.new.csv']
labelOriginAndDestination(history, liveDatas)