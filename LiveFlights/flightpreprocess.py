
def setUpFiles(flights_path = "C:\\Users\\remem\\Downloads\\flights\\sorted_2018-01-20-20_32.csv", stop_at_line = 110646):
    readfile = open(flights_path, "r")
    writefiletraining = open("C:\\Users\\remem\\Downloads\\flights\\training.csv", 'w')
    writefiletests = open("C:\\Users\\remem\\Downloads\\flights\\tests.csv", 'w')

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

def add_Origin_And_Destination(flights_file, origin_And_Destination_File, new_File ):
    flights = open(flights_file, 'r')

    #call sign, origin, destination
    origins_And_Destinations = open(origin_And_Destination_File, 'r')

    new_flights_file = open(new_File, 'w')

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

def remove_duplicates(old_file_name, new_file_name):
    line_set = set()
    old_file = open(old_file_name, 'r')
    new_file = open(new_file_name, 'w')
    duplicates_found = 0
    for line in old_file:
        if(line in line_set):
            duplicates_found += 1
        else:
            line_set.add(line)
            new_file.write(line)
    old_file.close()
    new_file.close()
    print "removed " + str(duplicates_found) + " elements"

#remove_duplicates("C:\\Users\\Resea\\Downloads\\flights\\live_2018-02-23-13_10.new.csv", "C:\\Users\\Resea\\Downloads\\flights\\live_2018-02-23-13_10.NoDups.csv" )



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
