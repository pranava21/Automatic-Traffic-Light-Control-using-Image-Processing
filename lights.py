import traffic
import RPi.GPIO as GPIO
import cam
import DB

road1 = traffic.Road('Road 1',23,17,27)
road2 = traffic.Road('Road 2',22,5,6)
road3 = traffic.Road('Road 3',24,19,26)
road4 = traffic.Road('Road 4',21,20,16)

def getRoad(roadID):
    if roadID == 1:
        return road1
    elif roadID == 2:
        return road2
    elif roadID == 3:
        return road3
    elif roadID == 4:
        return road4
try:
    while 1:
        roadID = DB.getMax()
        road = getRoad(roadID)
        while DB.checkMax(roadID) > 50:
            if road.isGreenOn():
                continue
            else:
                road.greenLight()
                while  not road.isGreenOn():
                    if road.isGreenOn():
                        break
        road.redLight()
        while  not road.isRedOn():
            if road.isRedOn():
                break
except KeyboardInterrupt:
    GPIO.cleanup()
        





