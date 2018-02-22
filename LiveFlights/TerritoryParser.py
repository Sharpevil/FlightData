def findMinAndMaxAltitudeAndLongitude(flights_path = "C:\\Users\\Resea\\Downloads\\flights\\sorted_2018-01-20-20_32.csv", stop_at_line = 110646):
    readfile = open(flights_path, "r")
    smallesLat = 20000000
    biggestLat = -2000000
    smallesLong = 20000000
    biggestLong = -2000000

    for line in readfile:
        lineList = line.split(',')
        latitude = (lineList[1])
        longitude = (lineList[2])
        latitude = float(latitude)
        longitude = float(longitude)

        if(latitude < smallesLat):
            smallesLat = latitude
        if(latitude > biggestLat):
            biggestLat = latitude
        if(longitude < smallesLong):
            smallesLong = longitude
        if(longitude > biggestLong):
            biggestLong = longitude

    print "Biggest Lat is : " + str(biggestLat)
    print "Smallest Lat is : " + str(smallesLat)
    print "Biggest Long is : " + str(biggestLong)
    print "Smallest Long is : " + str(smallesLong)

def parseTerritory(flights_path = "C:\\Users\\Resea\\Downloads\\flights\\sorted_2018-01-20-20_32.csv"):
    readfile = open(flights_path, "r")
    lineNum = 0
    for line in readfile:
        lineNum = lineNum + 1
        print lineNum
        lineList = line.split(',')
        latitude = (lineList[1])
        longitude = (lineList[2])
        latitude = latitude[:4]
        longitude = longitude[:5]
        latlong = latitude + ',' + longitude
        file = open("C:\\Users\\Resea\\Downloads\\flights\\ranges2\\" + latlong + ".csv", "a")
        file.write(line)
        file.close()

def parseTerritoryByCallSign(flights_path = "C:\\Users\\Resea\\Downloads\\flights\\sorted_2018-01-20-20_32.csv"):
    readfile = open(flights_path, "r")
    lineNum = 0
    for line in readfile:
        lineNum = lineNum + 1
        if((lineNum % 10000) == 0):
            print lineNum
        lineList = line.split(',')
        callSign = lineList[8]
        # causes an issue with flight signs who have a * in their name
        file = open("C:\\Users\\Resea\\Downloads\\flights\\callSigns\\" + callSign + ".csv", "a")
        file.write(line)
        file.close()

parseTerritoryByCallSign()


# for latitude in range(360,437,1):              #latitudes
#     for longitude in range(-792,-706,1):        #longitudes
#         latlong = str(float(latitude)/10) + ',' + str(float(longitude)/10)
#         open("C:\\Users\\Resea\\Downloads\\flights\\ranges\\" + latlong + ".csv", "w").close()
