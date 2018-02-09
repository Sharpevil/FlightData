# preprocess()

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

# num = 0
# for line in (open("C:\\Users\\remem\\Downloads\\flights\\tests.csv", 'r')):
#     num = num + 1
#
# print(num)