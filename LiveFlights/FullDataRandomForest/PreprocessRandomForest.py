from sklearn.externals import joblib
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

def setUpClassifierFiles(flights_path = "C:\\Users\\Resea\\Downloads\\flights\\live_2018-02-23-13_10.new.csv"):
    data = [None] * 100000
    labels = [None] * 100000
    fileNameBeginning = "Classifier"

    readfile = open(flights_path, "r")
    fileNum = 1
    lineNum = 0
    for line in readfile:
        values = line.split(',')
        lineList = line.split(',')#do stuff

        latitude = (lineList[1])
        longitude = (lineList[2])
        altitude = (lineList[3])
        heading = (lineList[9])
        airplane = lineList[7]
        #airCraftID = lineList[7]
        callSign = lineList[8]
        #ingestionTime = lineList[13]
        data[lineNum] = [latitude, longitude, altitude, heading]
        labels[lineNum] = callSign



        lineNum = lineNum + 1
        if(lineNum == 100000):
            lineNum = 0
            clf = tree.DecisionTreeClassifier()
            clf.fit(data, labels)
            joblib.dump(clf, 'C:\\Users\\Resea\\Downloads\\flights\\DecisionTrees\\' + fileNameBeginning + str(fileNum))
            print "Finished File Number " + str(fileNum)
            fileNum += 1

setUpClassifierFiles()
