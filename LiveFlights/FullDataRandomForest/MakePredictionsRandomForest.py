from sklearn.externals import joblib
from sklearn import tree

classifierPath = 'C:\\Users\\remem\\Downloads\\flights\\DecisionTrees\\Classifier'

# def loadClassifiers():
#     classifierPath = 'C:\\Users\\Resea\\Downloads\\flights\\DecisionTrees\\Classifier'
#     classifierNum = 1
#     clfList = [None] * 82
#
#     while classifierNum != 83:
#         clfList[classifierNum - 1] = joblib.load(classifierPath + str(classifierNum))
#         classifierNum += 1
#         print classifierNum
#
#     return clfList
#
# loadClassifiers()

floor_latitude = 5  # leaves two places after the decimal
floor_longitude = 6  # leaves two place after the decimal
floor_ground_speed = 3
floor_vertical_climb_rate = 5
floor_altitude = 3
floor_heading = 3

def predict(latitude, longitude, altitude, heading, ground_speed, vertical_climb_rate):
    classifierNum = 1
    map = {}
    callsign = ""
    map[""] = 0
    bestCallSign = callsign
    while classifierNum != 8266:
        clf = joblib.load(classifierPath + str(classifierNum))
        callsign = clf.predict([[latitude, longitude, altitude, heading, ground_speed, vertical_climb_rate]])[0]
        if(not(callsign in map.keys())):
            map[callsign] = 1
        else:
            map[callsign] = map[callsign] + 1
            if(map[bestCallSign] < map[callsign]):
                bestCallSign = callsign
                print callsign + ":  " + str(map[callsign]) + '//' + str(classifierNum)
            if("CMP808" in callsign):
                print callsign + ":  " + str(map[callsign]) + '//' + str(classifierNum)
                print bestCallSign + ":  " + str(map[bestCallSign]) + '//' + str(classifierNum) + "(Best call sign)"
        if(classifierNum%1000 == 0):
            print bestCallSign + ":  " + str(map[bestCallSign]) + '//' + str(classifierNum) + "(Best call sign)"
        classifierNum += 1
    for callsign in map.keys():
        if(map[callsign] > map[bestCallSign]):
            bestCallSign = callsign

    print map
    print bestCallSign
    return bestCallSign

def makePredictions():
    print predict(38.88639, -75.42914,22100, 188.0)

def score(fileName, stopAtLine = -1):
    file = open(fileName)
    lineNum = 0
    correctPredictions = 0
    totalPredictions = 0
    currentline = 0

    for line in file:
        currentline += 1
        if(currentline%100000 != 0):
            continue
        print line
        if(lineNum == stopAtLine):
            break
        else:
            lineNum += 1
            print lineNum
        lineList = line.split(',')  # do stuff

        latitude = (lineList[1])[:floor_latitude]
        longitude = (lineList[2])[:floor_longitude]
        altitude = (lineList[3])[:floor_altitude]
        heading = (lineList[9])[:floor_heading]
        ground_speed = (lineList[4])[:floor_ground_speed]
        vertical_climb_rate = lineList[5][:floor_vertical_climb_rate]

        callSign = lineList[8]

        predictedCallSign = predict(float(longitude), float(latitude), float(altitude), float(heading), float(ground_speed), float(vertical_climb_rate))

        if(predictedCallSign == callSign):
            correctPredictions += 1
        totalPredictions += 1

    return float(correctPredictions) / float(totalPredictions)


def printPartOfFile():
    for line in open('C:\\Users\\Resea\\Downloads\\flights\\live_2018-02-23-13_10.clean.csv'):
        print line

print score("C:\\Users\\remem\\Downloads\\flights\\sorted_2018-01-20-20_32.csv", 10)

