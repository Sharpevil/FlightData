FILE_NAME_CSV = "C:\\Users\\remem\\Downloads\\flights\\sorted_2018-01-20-20_32.csv"                      # must be replaced with path being used.
WRITE_FILE_NAME_CSV = "C:\\Users\\remem\\Downloads\\flights\\kml\\sorted_2018-01-20-20_32.kml"

file = open(FILE_NAME_CSV, "r")         # "r" means read mode

writefile = open(WRITE_FILE_NAME_CSV, "w")
writefile.write('''<?xml version="1.0" encoding="utf-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
	    <Style id="yellow">
	<LineStyle>
	<color>7f00ffff</color>
	<width>1</width>
	</LineStyle>
	<PolyStyle>
	<color>7f00ff00</color>
	</PolyStyle>
	</Style>
	
		<Style id="red">
	<LineStyle>
	<color>7f0000ff</color>
	<width>1</width>
	</LineStyle>
	<PolyStyle>
	<color>00000000</color>
	</PolyStyle>
	</Style>
	
	    <Style id="blue">
	<LineStyle>
	<color>7fff0000</color>
	<width>1</width>
	</LineStyle>
	<PolyStyle>
	<color>7fff0000</color>
	</PolyStyle>
	</Style>
	
	    <Style id="green">
	<LineStyle>
	<color>7f00ff00</color>
	<width>1</width>
	</LineStyle>
	<PolyStyle>
	<color>7f00ff00</color>
	</PolyStyle>
	</Style>

	''')
entry = ""

lastAirCraftID = ""

lineNum = 0
for line in file:
    print (lineNum)
    lineNum = lineNum + 1
    lineList = line.split(",")#do stuff

    latitude = lineList[1]
    longitude = lineList[2]
    altitude = lineList[3]
    heading = float(lineList[9])
    airCraftID = lineList[8]

    if((airCraftID != lastAirCraftID)):
        if(lineNum != 1):
            writefile.write('''</coordinates>\n\t</LineString>\n\t</Placemark>\n	<Placemark>\n''')
        else:
            writefile.write('''<Placemark>\n ''')

        #uncomment and comment the color = yellow part to color paths based on direction. 
        if(heading < 90):
            color = "blue"
        elif(heading < 180):
            color = "red"
        elif(heading < 270):
            color = "yellow"
        else:
            color = "green"
        # color = "yellow"

        writefile.write("\t<name>" + airCraftID + "</name>\n" )
        writefile.write("\t<description>" + airCraftID + "</description>\n" )
        writefile.write("\t<styleUrl>#" + color + "</styleUrl>\n")
        writefile.write("\t<LineString>\n\t<altitudeMode>absolute</altitudeMode>\n")
        writefile.write("\t\t<coordinates>")

    writefile.write(longitude + ',' + latitude + ',' + altitude + ' ')

    if(lineNum == 1047266): #110646): #1047266*/):
        break



    lastAirCraftID = lineList[8]



    ingestionTime = lineList[13]

writefile.write('''\t\t</coordinates>\n\t</LineString>\n\t</Placemark>\n''')
writefile.write('''</Document>
</kml>''')
