
def setUpFiles(flights_path = "C:\\Users\\Resea\\Downloads\\flights\\sorted_2018-01-20-20_32.csv", stop_at_line = 110646):
    readfile = open(flights_path, "r")
    writefiletraining = open("C:\\Users\\Resea\\Downloads\\flights\\training.csv", 'w')
    writefiletests = open("C:\\Users\\Resea\\Downloads\\flights\\tests.csv", 'w')

    lineNum = 0
    for line in readfile:

        if(lineNum % 20 == 0):
            writefiletests.write(line)
        else:
            writefiletraining.write(line)

        lineNum = lineNum + 1
        if (lineNum == stop_at_line):  # 110646): #1047266*/):
            writefiletraining.close()
            writefiletests.close()
            break

    writefiletraining.close()
    writefiletests.close()

def add_Origin_And_Destination(flights_file = "C:\\Users\\Resea\\Downloads\\flights\\sorted_2018-01-20-20_32.csv", origin_And_Destination_File = "C:\\Users\\remem\\Downloads\\flights\\callsign_airports.csv" ):
    flights = open(flights_file, 'r')

    #call sign, origin, destination
    origins_And_Destinations = open(origin_And_Destination_File, 'r')

    new_flights_file = open("C:\\Users\\Resea\\Downloads\\flights\\ODsorted_2018-01-20-20_32.csv", 'w')

    origins_Map = {}
    destinations_Map = {}
    for line in origins_And_Destinations:
        values = line.split(',')
        callSign = values[0]
    print('starting to change files')
    linenum =0
    for line in flights:
        values = line.split(',')
        if(values[8] in origins_Map.keys()):
            linenum = linenum + 1
            print(linenum)
            len(line)
            newString = line[:len(line) -2] + ',' + origins_Map.get(values[8]) + ',' + destinations_Map.get(values[8])
            #print(newString)
            new_flights_file.write(newString)

# add_Origin_And_Destination()
# linenum = 0
# for line in open("C:\\Users\\remem\\Downloads\\flights\\ODsorted_2018-01-20-20_32.csv", 'r'):
#     linenum = linenum + 1
#     print(line)
#     if(linenum == 500):
#         break


# num = 0
# for line in (open("C:\\Users\\remem\\Downloads\\flights\\tests.csv", 'r')):
#     num = num + 1
#
# print(num)
