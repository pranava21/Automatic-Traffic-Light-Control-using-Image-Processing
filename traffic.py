import time
import RPi.GPIO as GPIO
import cv2
import numpy as np
import random
import mysql.connector
import socket

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Road:
    def __init__(self, name, red, yellow, green):
        self.name = name
        self.red = red
        self.yellow = yellow
        self.green = green

        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(yellow, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        
        GPIO.output(red, True)
        GPIO.output(yellow,False)
        GPIO.output(green, False)

    def redOn(self):
        GPIO.output(self.red, True)

    def redOff(self):
        GPIO.output(self.red, False)

    def greenOn(self):
        GPIO.output(self.green, True)

    def greenOff(self):
        GPIO.output(self.green, False)

    def isGreenOn(self):
        if GPIO.input(self.green) == 1:
            return True
        else:
            return False
            
    def isRedOn(self):
        if GPIO.input(self.red) == 1:
            return True
        else:
            return False
                
    
    def redLight(self):
        ## Considering Green is On, and Road will be red lit.
        GPIO.output(self.green, False)
        time.sleep(1)
        GPIO.output(self.yellow, True)
        time.sleep(2)
        GPIO.output(self.yellow, False)
        time.sleep(1)
        GPIO.output(self.red, True)

    def greenLight(self):
        ## Considering Red is On, and Road will be Green lit.
        GPIO.output(self.red, False)
        time.sleep(1)
        GPIO.output(self.yellow, True)
        time.sleep(2)
        GPIO.output(self.yellow, False)
        time.sleep(1)
        GPIO.output(self.green, True)

