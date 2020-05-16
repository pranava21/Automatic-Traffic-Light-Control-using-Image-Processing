import RPi.GPIO as GPIO
import serial
import trafficControl as tc

ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    while 1:
        isAmbulanceThere = tc.checkIfAmbulance(ser)
        print(isAmbulanceThere)
        if isAmbulanceThere != 0:
            tc.controlAmbulance(ser)

        else:
            tc.controlTraffic(ser)
except KeyboardInterrupt:
    GPIO.cleanup()
