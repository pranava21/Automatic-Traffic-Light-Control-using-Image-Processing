import RPi.GPIO as GPIO
import serial
import trafficControl as tc
import DB

ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    DB.setI(1)
    while 1:
        isAmbulanceThere = tc.checkIfAmbulance(ser)
        # print(isAmbulanceThere)
        if isAmbulanceThere != 0:
            tc.controlAmbulance(ser)

        else:
            DB.incrementI()
            if DB.getI() > 4:
                DB.setI(2)
            tc.controlTraffic(ser, DB.getI())
except KeyboardInterrupt:
    GPIO.cleanup()
