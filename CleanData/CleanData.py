def cleanAltitude(inFilePath, outFilePath):
    inFile = open(inFilePath, 'r')
    outFile = open(outFilePath, 'w')

    finishedLines = 0
    writtenLines = 0


    for line in inFile:
        if(finishedLines%100000 == 0):
            print finishedLines
        data = line.split(',')
        altitude = data[3]
        altitude = int(altitude)

        if(altitude > -1 and altitude < 50001):
            outFile.write(line)
            writtenLines = writtenLines + 1

        finishedLines = finishedLines + 1

    print writtenLines


        # if(altitude < 1):
        #     print "Low altitude is:     " + str (altitude)
        # if (altitude > largestAltitude and altitude < 60000):
        #     largestAltitude = altitude
        # allAltitudes = allAltitudes + altitude

#    print "Largest Altitude is :    " + str(largestAltitude)
#    print "Average Altitdue is :    " + str(allAltitudes/9978637)

    #
    #
    # Gives 9978637 lines
def cleanCreationTime(inFilePath, outFilePath):
    inFile = open(inFilePath, 'r')
    outFile = open(outFilePath, 'w')
    finishedLines = 0
    outputtedLines = 0

    for line in inFile:

        if(finishedLines%100000 == 0):
            print finishedLines
        finishedLines = finishedLines + 1
        data = line.split(',')
        messageTime = data[0]
        ingestionTime = data[13]
        creationTime = int(ingestionTime) - int(messageTime)
        if(not (creationTime > 70000)):
            outFile.write(line)
            outputtedLines = outputtedLines + 1

    print "Lines outputted to file:     " + str(outputtedLines)

    #
    #
    #
cleanAltitude(inFilePath = "C:\\Users\\Resea\\Downloads\\flights\\CreationCleanedSorted_2018-01-20-20_32.csv", outFilePath = "C:\\Users\\Resea\\Downloads\\flights\\CleanAltitudeSorted_2018-01-20-20_32.csv")
