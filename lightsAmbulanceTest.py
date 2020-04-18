import traffic
import RPi.GPIO as GPIO
import cam
import DB
import serial

ser = serial.Serial('/dev/ttyACM1',9600)

road1 = traffic.Road('1',23,17,27)
road2 = traffic.Road('2',22,5,6)
road3 = traffic.Road('3',24,19,26)
road4 = traffic.Road('4',21,20,16)

def getRoad(roadID):
    if roadID == 1:
        return road1
    elif roadID == 2:
        return road2
    elif roadID == 3:
        return road3
    elif roadID == 4:
        return road4

def checkIfAmbulance():
    a = int(ser.readline().decode())
    print(a)
    return(a)

def checkIfLightIsOn(light):
        if light == "red":
            while not road.isRedOn():
                if road.isRedOn():
                    break
        elif light == "green":
            while  not road.isGreenOn():
                if road.isGreenOn():
                    break
            
            
    
try:
    while 1:
        isAmbulanceThere = checkIfAmbulance()
        if isAmbulanceThere != 0:
            print("In Ambulance Loop")
            roadID = isAmbulanceThere
            road = getRoad(roadID)
            while checkIfAmbulance() == roadID:
                if road.isGreenOn():
                    continue
                else:
                    road.greenLight()
                    checkIfLightIsOn("green")
            road.redLight()
            checkIfLightIsOn("red")
                    
            
        else:
            print("In Usual Loop")
            roadID = DB.getMax()
            road = getRoad(roadID)
            while DB.checkMax(roadID) > 50:
                if road.isGreenOn():
                    if checkIfAmbulance() == roadID:
                        continue
                    
                    elif checkIfAmbulance() != 0:
                        print("Checking for A in usual loop")
                        road.redLight()
                        checkIfLightIsOn("red")
                        break
                    
                    else:
                        continue
                else:
                    road.greenLight()
                    checkIfLightIsOn("green")
            if road.isRedOn():
                continue
            else:
                road.redLight()
                checkIfLightIsOn("red")
except KeyboardInterrupt:
    GPIO.cleanup()
        





