def getHistory(historyPath = r"C:\Users\Resea\Downloads\flights\newHistory.csv"):
    historyFile = open(historyPath)
    for line in historyFile:
        end = 1
        #TODO create a map of call signs to sets of time with origin and destination associated with the time
        