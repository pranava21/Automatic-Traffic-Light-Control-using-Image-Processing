import RPi.GPIO as GPIO
import serial
import trafficControl as tc

ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    i = 1
    while 1:
        isAmbulanceThere = tc.checkIfAmbulance(ser)
        print(isAmbulanceThere)
        if isAmbulanceThere != 0:
            tc.controlAmbulance(ser)

        else:
            i += 1
            if i > 4:
                i = 2
            tc.controlTraffic(ser, i)
except KeyboardInterrupt:
    GPIO.cleanup()
