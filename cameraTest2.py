import cv2
import numpy as np
from time import sleep
import DB
import socket
import cam
import UDP

UDP_IP = "192.168.1.20"
##UDP_IP = "192.168.43.144"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
    
trafficCam1 = cv2.VideoCapture(0)
if not trafficCam1.isOpened():
    trafficCam1 = cv2.VideoCapture(1)

trafficCam2 = cv2.VideoCapture(2)

while 1:
    ret1, frame1 = trafficCam1.read()
    ret2, frame2 = trafficCam2.read()
        
    sortedTraffic12 = cam.getTrafficDensityFromImages(frame1, frame2)
    
    sortedTraffic34, address = sock.recvfrom(2048)
    
    sortedTraffic34 = UDP.processData(sortedTraffic34)

    print("Traffic on 1 and 2: " + str(sortedTraffic12))
    print("Traffic on 3 and 4: " + str(sortedTraffic34))
    print(" ")
    
    DB.updateTraffic(sortedTraffic12, sortedTraffic34)
    
    sleep(0.5)
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

trafficCam1.release()
trafficCam2.release()
cv2.destroyAllWindows()

