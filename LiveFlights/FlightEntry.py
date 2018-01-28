class FlightEntry:
    def __init__(self, messageTime, latitude, longitude, altitude, heading, groundSpeed, verticalClimbRate, squawkCode, airCraftID, callSign, trackNumber, alertFlag
                 , emergencyFlag, isOnGroundFlag, ingestionTime):
        self.messageTime = messageTime
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.heading = heading
        self.groundSpeed = groundSpeed
        self.verticalClimbRate = verticalClimbRate
        self.squawkCode = squawkCode
        self.airCraftID = airCraftID
        self.callSign = callSign
        self.trackNumber = trackNumber
        self.alertFlag = alertFlag
        self.emergencyFlag = emergencyFlag
        self.isOnGroundFlag = isOnGroundFlag
        self.ingestionTime = ingestionTime




#1. message time (unix time - use https://www.epochconverter.com/ to convert to human readable format)
#2: latitude (degrees)
#3: longitude (degrees)
#4: altitude (feet)
#5: heading (degrees)
#6: ground speed
#7: vertical climb rate
#8: squawk code
#9: aircraft id (hexadecimal ID, unique to a particular flight)
#10: call sign
#11: track number
#12: alert flag
#13: emergency flag
#14: is on ground flag
#15: ingestion time (unix time - use https://www.epochconverter.com/ to convert to human readable format)