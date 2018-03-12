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

    floor_latitude = 5  # leaves two places after the decimal
    floor_longitude = 6  # leaves two place after the decimal
    floor_ground_speed = 3
    floor_vertical_climb_rate = 5
    floor_altitude = 3
    floor_heading = 3


    for line in open("C:\\Users\\remem\\Downloads\\flights\\shuffled.new.csv", 'r'):
        lineList = line.split(',')#do stuff

        latitude = (lineList[1])[:floor_latitude]
        longitude = (lineList[2])[:floor_longitude]
        altitude = (lineList[3])[:floor_altitude]
        heading = (lineList[9])[:floor_heading]
        ground_speed = (lineList[4])[:floor_ground_speed]
        vertical_climb_rate = lineList[5][:floor_vertical_climb_rate]


        #airCraftID = lineList[7]
        callSign = lineList[8]
        #ingestionTime = lineList[13]
        data[lineNum] = [float(latitude), float(longitude), float(altitude), float(heading), float(ground_speed), float(vertical_climb_rate)]
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
