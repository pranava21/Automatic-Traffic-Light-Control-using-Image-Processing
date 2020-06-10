import traffic
import DB
from Timer import Timer
import time

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


def controlTraffic(ser, i):
    print("In Control Loop")
    timer = Timer()
    roadID = DB.getMax()
    road = getRoad(roadID)
    while DB.checkMax(roadID) > 50:
        if road.isGreenOn():
            elapsedTime = timer.calculateTimeElapsed()

            if checkIfAmbulance(ser) == roadID:
                continue

            elif checkIfAmbulance(ser) != 0:
                print("Checking for A in Control loop")
                road.redLight()
                checkIfLightIsOn("red", road)
                break

            elif elapsedTime >= 10.0:
                id = DB.getTrafficDensityinOrder(DB.getI())
                if DB.checkMax(id) > 50:
                    road.redLight()
                    timer.stopTimer()
                    time.sleep(2)
                    print("Road with " + str(DB.getI()) + " Highest Traffic Density")
                    ifTimerRunsOut(ser, DB.getI())
                    break
                else:
                    print("No traffic " + str(DB.getI()))
                    timer.stopTimer()
                    timer.startTimer()
                    DB.incrementI()
                    if DB.getI() > 4:
                        DB.setI(2)

            else:
                continue
        else:
            road.greenLight()
            checkIfLightIsOn("green", road)
            timer.startTimer()
    if road.isRedOn():
        red = True
    else:
        road.redLight()
        checkIfLightIsOn("red", road)


def ifTimerRunsOut(ser, i):
    timer = Timer()
    if i == 2:
        roadID = DB.getSecondHighest()
    elif i == 3:
        roadID = DB.getThirdHighest()
    else:
        roadID = DB.getLeast()

    road = getRoad(roadID)
    while DB.checkMax(roadID) > 50:
        if road.isGreenOn():
            elapsedTime = timer.calculateTimeElapsed()

            if checkIfAmbulance(ser) == roadID:
                continue

            elif checkIfAmbulance(ser) != 0:
                print("Checking for A in Control loop")
                road.redLight()
                checkIfLightIsOn("red", road)
                break

            elif elapsedTime >= 5.0:
                road.redLight()
                timer.stopTimer()
                time.sleep(2)
                break

            else:
                continue
        else:
            road.greenLight()
            checkIfLightIsOn("green", road)
            timer.startTimer()
    if road.isRedOn():
        red = True
    else:
        road.redLight()
        checkIfLightIsOn("red", road)
