from sklearn.externals import joblib
from sklearn import tree

classifierPath = 'C:\\Users\\Resea\\Downloads\\flights\\DecisionTrees\\Classifier'

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

def predict(latitude, longitude, altitude, heading):
    classifierNum = 1
    map = {}

    while classifierNum != 80:
        clf = joblib.load(classifierPath + str(classifierNum))
        callsign = clf.predict([[latitude, longitude, altitude, heading]])[0]
        if(callsign == "JBU874"):
            print classifierPath + str(classifierNum)
        if(not(callsign in map.keys())):
            map[callsign] = 1
        else:
            map[callsign] = map[callsign] + 1
        classifierNum += 1
    bestCallSign = callsign
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

        latitude = (lineList[1])
        longitude = (lineList[2])
        altitude = (lineList[3])
        heading = (lineList[9])
        callSign = lineList[8]

        predictedCallSign = predict(longitude, latitude, altitude, heading)

        if(predictedCallSign == callSign):
            correctPredictions += 1
        totalPredictions += 1

    return float(correctPredictions) / float(totalPredictions)


def printPartOfFile():
    for line in open('C:\\Users\\Resea\\Downloads\\flights\\live_2018-02-23-13_10.clean.csv'):
        print line

print score("C:\\Users\\Resea\\Downloads\\flights\\sorted_2018-01-20-20_32.csv", 10)