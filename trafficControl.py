import traffic
import DB

road1 = traffic.Road('1', 23, 17, 27)
road2 = traffic.Road('2', 22, 5, 6)
road3 = traffic.Road('3', 24, 19, 26)
road4 = traffic.Road('4', 21, 20, 16)


def getRoad(roadID):
    if roadID == 1:
        return road1
    elif roadID == 2:
        return road2
    elif roadID == 3:
        return road3
    elif roadID == 4:
        return road4


def checkIfAmbulance(ser):
    return int(ser.readline().decode())



def checkIfLightIsOn(light, road):
    if light == "red":
        while not road.isRedOn():
            if road.isRedOn():
                break
    elif light == "green":
        while not road.isGreenOn():
            if road.isGreenOn():
                break


def controlAmbulance(ser):
    print("In Ambulance Loop")
    roadID = checkIfAmbulance(ser)
    print(roadID)
    road = getRoad(roadID)
    while checkIfAmbulance(ser) == roadID:
        if road.isGreenOn():
            print("Checking if Green Light is On in Ambulance Loop")
            continue
        else:
            print("Turing On Green Light")
            road.greenLight()
            checkIfLightIsOn("green", road)
    print("Turning On Red Light")
    road.redLight()
    checkIfLightIsOn("red", road)


def controlTraffic(ser):
    print("In Control Loop")
    roadID = DB.getMax()
    road = getRoad(roadID)
    while DB.checkMax(roadID) > 50:
        if road.isGreenOn():
            if checkIfAmbulance(ser) == roadID:
                continue

            elif checkIfAmbulance(ser) != 0:
                print("Checking for A in Control loop")
                road.redLight()
                checkIfLightIsOn("red", road)
                break

            else:
                continue
        else:
            road.greenLight()
            checkIfLightIsOn("green", road)
    if road.isRedOn():
        red = True
    else:
        road.redLight()
        checkIfLightIsOn("red", road)
