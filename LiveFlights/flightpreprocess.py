from sklearn import tree

num_of_test_flights = 5533
num_of_flights = 110646-5533


def preprocess(flights_path = "C:\\Users\\remem\\Downloads\\flights\\training.csv", test_flights_path = "C:\\Users\\remem\\Downloads\\flights\\tests.csv"):
    # df = pd.read_csv(flights_file, usecols=[1, 2, 3, 9])
    # print(type(df))
    # print(type (df.))
    # print(type(df[0][0]))

    alldata = [None]*num_of_flights
    alllabels = [None]*num_of_flights
    lineNum = 0
    flights_file = open(flights_path)
    for line in flights_file:
        if(lineNum%1000 == 0):
            print(lineNum)

        lineList = line.split(',')#do stuff

        #messageTime = lineList[0]
        if(len(lineList) > 1):
            latitude = (lineList[1])
            longitude = (lineList[2])
            altitude = (lineList[3])
            heading = (lineList[9])
            #airCraftID = lineList[7]
            callSign = lineList[8]
            #ingestionTime = lineList[13]

            data = [float(latitude) , float(longitude), float(altitude), float(heading)]
            label = callSign
            alldata[lineNum] = data
            alllabels[lineNum ] = label
            lineNum = lineNum + 1

        if (lineNum == 110646):  # 110646): #1047266*/):
            break
    # print( len(alldata))
    # print(len(alllabels))
    # print(alllabels)
    clf = tree.DecisionTreeClassifier()
    clf.fit(alldata,
            alllabels
            )

    test_flights_file = open(test_flights_path)
    alltestdata = [None]*num_of_test_flights
    alltestlabels = [None]*num_of_test_flights
    lineNum = 0

    for line in test_flights_file:
        lineList = line.split(',')#do stuff
        latitude = (lineList[1])
        longitude = (lineList[2])
        altitude = (lineList[3])
        heading = (lineList[9])
        # airCraftID = lineList[7]
        callSign = lineList[8]
        # ingestionTime = lineList[13]

        data = [float(latitude), float(longitude), float(altitude), float(heading)]
        label = callSign
        alltestdata[lineNum] = data
        alltestlabels[lineNum] = label
        lineNum = lineNum + 1

    print(clf.score(alltestdata, alltestlabels))
    print(clf.predict([[39.20906,-71.62375,38000,298.0]]))

# preprocess()

def setUpFiles(flights_path = "C:\\Users\\remem\\Downloads\\flights\\sorted_2018-01-20-20_32.csv"):
    readfile = open(flights_path, "r")
    writefiletraining = open("C:\\Users\\remem\\Downloads\\flights\\training.csv", 'w')
    writefiletests = open("C:\\Users\\remem\\Downloads\\flights\\tests.csv", 'w')

    lineNum = 0
    for line in readfile:

        if(lineNum % 20 == 0):
            writefiletests.write(line)
        else:
            writefiletraining.write(line)

        lineNum = lineNum + 1
        if (lineNum == 110646):  # 110646): #1047266*/):
            writefiletraining.close()
            writefiletests.close()
            break

preprocess()
# num = 0
# for line in (open("C:\\Users\\remem\\Downloads\\flights\\tests.csv", 'r')):
#     num = num + 1
#
# print(num)