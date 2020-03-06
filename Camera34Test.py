import socket
import time
import random
import cv2
import numpy as np
##IP address should be that of the device that is receiving
UDP_IP = "192.168.1.20"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
trafficCam1 = cv2.VideoCapture(0)
while True:
    ret1, frame1 = trafficCam1.read()
    hsvImage1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    lightGray = np.uint8([[[0,50,0]]])
    darkGray = np.uint8([[[179,50,255]]])
    mask1 = cv2.inRange(hsvImage1, lightGray, darkGray)
    result1 = cv2.bitwise_and(frame1, frame1, mask = mask1)
    grayImage1 = cv2.cvtColor(result1, cv2.COLOR_BGR2GRAY)
    edgedImage1 = cv2.Canny(grayImage1, 30, 200)
    contours1, hierarchy1 = cv2.findContours(edgedImage1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(result1, contours1, -1, (0,255,0), 2)
    #cv2.imshow('Contours1',result1)
    trafficOnRoad1 = str(len(contours1))
    trafficOnRoad2 = str(random.randint(50,100))
    MESSAGE = str(trafficOnRoad1) + " " + str(trafficOnRoad2)
    sock.sendto(MESSAGE.encode(), (UDP_IP,UDP_PORT))
                                                      
