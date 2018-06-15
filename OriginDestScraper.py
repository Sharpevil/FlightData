import json
from requests import get
from bs4 import BeautifulSoup

def scrape(callSign):
    url = "https://flightaware.com/live/flight/" + callSign
    page = get(url, stream=True).content
    html = BeautifulSoup(page, 'html.parser')
    allScripts = html.findAll('script')
    for script in allScripts:
        if 'var trackpollBootstrap =' in str(script):
            data = str(script)
            break
    data = data[data.index('{'):len(data)-10]
    jData = json.loads(str(data))
    splitJData = str(jData["flights"]).split()
    i = 1
    origin = ""
    while i < 10:
        nextPiece = splitJData[splitJData.index("'friendlyLocation':")+i]
        if nextPiece == "'coord':":
            break
        origin += splitJData[splitJData.index("'friendlyLocation':")+i]
        i += 1
    origin = origin[1:len(origin)-2]

    oCoords1 = splitJData[splitJData.index("'coord':") + 1]
    oCoords1 = oCoords1[1:len(oCoords1) - 1]
    oCoords2 = splitJData[splitJData.index("'coord':") + 2]
    oCoords2 = oCoords2[0:len(oCoords2) - 2]

    destJDataImp = splitJData[splitJData.index("'destination':"):]
    j = 1
    destination = ""
    while j < 10:
        nextPiece = destJDataImp[destJDataImp.index("'friendlyLocation':") + j]
        if nextPiece == "'coord':":
            break
        destination += destJDataImp[destJDataImp.index("'friendlyLocation':") + j]
        j += 1
    destination = destination[1:len(destination) - 2]

    dCoords1 = destJDataImp[destJDataImp.index("'coord':")+1]
    dCoords1 = dCoords1[1:len(dCoords1)-1]
    dCoords2 = destJDataImp[destJDataImp.index("'coord':") + 2]
    dCoords2 = dCoords1[0:len(dCoords2) - 2]

    return {"Origin":origin, "Destination":destination, "OriginCoords":[oCoords1, oCoords2],"DestCoords":[dCoords1,dCoords2]}

print(scrape('N179JA'))