import pickle
#import cPickle
import numpy as np
import pandas as pd



from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.naive_bayes import  GaussianNB


FILE_NAME_CSV = "C:\\Users\\remem\\Downloads\\sorted_2018-01-20-20_32.csv"

#8 is the label
df = pd.read_csv(FILE_NAME_CSV, usecols=[1,2,3,9])
dflabel = pd.read_csv(FILE_NAME_CSV, usecols=[8])

#file = open(FILE_NAME_CSV, "r")         # "r" means read mode
#alldata = []
#alllabels = []

lineNum = 0
# for line in file:
#     lineNum = lineNum + 1
#     if(lineNum%1000 == 0):
#         print(lineNum)
#     lineList = line.split(",")#do stuff
#
#     messageTime = lineList[0]
#     latitude = (lineList[1])
#     longitude = (lineList[2])
#     altitude = (lineList[3])
#     heading = (lineList[9])
#     airCraftID = lineList[7]
#     callSign = lineList[9]
#     ingestionTime = lineList[13]
#
#     data = latitude + longitude + altitude + heading
#     label = callSign
#     alldata.append(data)
#     alllabels.append(label)
#
#     if (lineNum == 110646):  # 110646): #1047266*/):
#         print(lineNum)
#         break
#
# alldata = np.array(alldata)
# alllabels = np.array(alllabels)
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(df, dflabel,test_size=0.5, random_state=42)
print("Done training1")

vectorizer=TfidfVectorizer(sublinear_tf=True,max_df=0.5,stop_words='english')
features_train_transformed = vectorizer.fit_transform(features_train)
features_test_transformed = vectorizer.transform(features_test)
print("Done training2")

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train_transformed = vectorizer.fit_transform(features_train)
features_test_transformed = vectorizer.transform(features_test)

print("Done training3")

### feature selection, because text is super high dimensional and
### can be really computationally chewy as a result
selector = SelectPercentile(f_classif, percentile=10)
selector.fit(features_train_transformed, labels_train)
features_train_transformed = selector.transform(features_train_transformed).toarray()
features_test_transformed = selector.transform(features_test_transformed).toarray()
print("Done training4")

clf = GaussianNB()
clf.fit(features_train_transformed, labels_train)#(features_train_transformed, labels_train)

print("Done fitting")

print(clf.score(features_test, labels_test))#features_test, labels_test))# for test




# 1. message time (unix time - use https://www.epochconverter.com/ to convert to human readable format)
# 2: latitude (degrees)
# 3: longitude (degrees)
# 4: altitude (feet)
# 5: ground speed (knots)
# 6: vertical climb rate (feet/min)
# 7: squawk code
# 8: aircraft id (hexadecimal ID, unique to a particular flight)
# 9: call sign
# 10: heading (degrees)
# 11: alert flag
# 12: emergency flag
# 13: is on ground flag
# 14: ingestion time (unix time - use https://www.epochconverter.com/ to convert to human readable format)

