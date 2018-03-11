from sklearn.externals import joblib
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
import random
flights_path = "C:\\Users\\remem\\Downloads\\flights\\live_2018-02-23-13_10.new.csv"
count = 8265579


def setUpClassifierFiles():
    fileNameBeginning = "Classifier"
    fileNum = 1
    data = [None] * 1000
    labels = [None] * 1000
    lineNum = 0


    for line in open("C:\\Users\\remem\\Downloads\\flights\\shuffled.new.csv", 'r'):
        lineList = line.split(',')#do stuff

        latitude = (lineList[1])
        longitude = (lineList[2])
        altitude = (lineList[3])
        heading = (lineList[9])
        #airCraftID = lineList[7]
        callSign = lineList[8]
        #ingestionTime = lineList[13]
        data[lineNum] = [latitude, longitude, altitude, heading]
        labels[lineNum] = callSign
        lineNum += 1

        if(lineNum == 1000):
            lineNum = 0
            clf = tree.DecisionTreeClassifier()
            clf.fit(data, labels)
            joblib.dump(clf, 'C:\\Users\\remem\\Downloads\\flights\\DecisionTrees\\' + fileNameBeginning + str(fileNum))
            print("Finished File Number " + str(fileNum))
            fileNum += 1

def shuffleFile(readfile = "C:\\Users\\remem\\Downloads\\flights\\live_2018-02-23-13_10.new.csv", writefile = "C:\\Users\\remem\\Downloads\\flights\\shuffled.new.csv" ):
    fid = open(readfile, "r")
    li = fid.readlines()
    fid.close()
    print "read done"

    random.shuffle(li)
    print("shuffle done")

    fid = open(writefile, "w")
    fid.writelines(li)
    fid.close()

setUpClassifierFiles()
