from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from LiveFlights.flightpreprocess import setUpFiles

# the percentages were based on running the data on a csv file that was sorted by the plane (airCraftID)
def runPredictions(setupFiles = True, test_size = 5533, data_size = (110646- 5533), train_flights_path = "C:\\Users\\Resea\\Downloads\\flights\\training.csv", test_flights_path = "C:\\Users\\remem\\Downloads\\flights\\tests.csv"):
    if(setupFiles):
        setUpFiles(stop_at_line = test_size + data_size)

    alldata = [None]*data_size
    alllabels = [None]*data_size
    lineNum = 0
    train_flights_file = open(train_flights_path)
    for line in train_flights_file:
        if(lineNum%100000 == 0):
            print(lineNum)

        lineList = line.split(',')#do stuff

        latitude = (lineList[1])
        longitude = (lineList[2])
        altitude = (lineList[3])
        heading = (lineList[9])
        airplane = lineList[7]
        #airCraftID = lineList[7]
        callSign = lineList[8]
        #ingestionTime = lineList[13]

        data = [float(latitude) , float(longitude), float(altitude), float(heading)]
        label = callSign
        alldata[lineNum] = data
        alllabels[lineNum ] = label
        lineNum = lineNum + 1

    train_flights_file.close()
    clf = tree.DecisionTreeClassifier()# 94.5% on 1% of the data for latitude, longitude, altitude, heading
    #clf = GaussianNB() // 51.166%       on 1% of the data for latitude, longitude, altitude, heading
    clf.fit(alldata,
            alllabels
            )

    test_flights_file = open(test_flights_path)
    alltestdata = [None]*test_size
    alltestlabels = [None]*test_size
    lineNum = 0

    for line in test_flights_file:
        lineList = line.split(',')#do stuff
        latitude = (lineList[1])
        longitude = (lineList[2])
        altitude = (lineList[3])
        heading = (lineList[9])
        airplane = lineList[7]
        # airCraftID = lineList[7]
        callSign = lineList[8]
        # ingestionTime = lineList[13]

        data = [float(latitude), float(longitude), float(altitude), float(heading)]
        label = callSign
        alltestdata[lineNum] = data
        alltestlabels[lineNum] = label
        lineNum = lineNum + 1

    test_flights_file.close()
    print(clf.score(alltestdata, alltestlabels))
    # print(clf.predict([[40.88768,-75.68646,11825,180.0]]))
    # print("Should be SAA203")

#0.946502801374
onepercenttestsize = 5533
#0.858261400962
tenpercenttestsize = 52364
fulltestsize = 500000


#twenty percent - 0.8156

#twenty-five percent - 0.805128

#26.25% - 0.802392380952

#27.5 %    - MemoryError: could not allocate 32044482560 bytes

#thirty percent - MemoryError: could not allocate 34846277632 bytes



onepercentdatasize = 110646 - 5533
tenpercentdatasize = 1047266 - 52364
fulldatasize = 9500000


runPredictions(setupFiles = False,test_size = onepercenttestsize, data_size = onepercentdatasize)

#cuda
