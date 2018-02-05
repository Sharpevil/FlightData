FILE_NAME_CSV = "C:\\Users\\remem\\Downloads\\sorted_2018-01-20-20_32"                      # must be replaced with path being used.

file = open(FILE_NAME_CSV, "r")         # "r" means read mode
flights = {}

lineNum = 0
for line in file:
    lineNum = lineNum + 1
    print(lineNum)
    lineList = line.split(",")#do stuff

    messageTime = lineList[0]
    latitude = lineList[1]
    longitude = lineList[2]
    altitude = lineList[3]
    heading = float(lineList[9])
    airCraftID = lineList[7]

    if(airCraftID in flights):
        flights[airCraftID] = flights[airCraftID] + '\n' + line
    else:
        flights[airCraftID] = line

    ingestionTime = lineList[13]

print(flights)

#1. message time (unix time - use https://www.epochconverter.com/ to convert to human readable format)
#2: latitude (degrees)
#3: longitude (degrees)
#4: altitude (feet)
#5: heading (degrees)
#6: ground speed
#7: vertical climb rate
#8: squawk code
#9: aircraft id (hexadecimal ID, unique to a particular flight)     # actually seems to be heading
#10: call sign
#11: track number
#12: alert flag
#13: emergency flag
#14: is on ground flag
#15: ingestion time (unix time - use https://www.epochconverter.com/ to convert to human readable format)

