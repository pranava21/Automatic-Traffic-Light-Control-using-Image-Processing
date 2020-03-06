import cv2
import numpy as np
import time
import traffic
import DB
import cam
import socket
import UDP

UDP_IP = "192.168.1.20"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
    
trafficCam1 = cv2.VideoCapture(0)
trafficCam2 = cv2.VideoCapture(2)

try:
    while 1:
        ret1, frame1 = trafficCam1.read()
        ret2, frame2 = trafficCam2.read()
            
        sortedTraffic12 = cam.camera(frame1, frame2)
        sortedTraffic34, address = sock.recvfrom(2048)
        sortedTraffic34 = UDP.recvData(sortedTraffic34)
        
        DB.updateTraffic(sortedTraffic12, sortedTraffic34)
        time.sleep(0.5)
            
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

except KeyboardInterrupt:
    trafficCam1.release()
    trafficCam2.release()
    cv2.destroyAllWindows()

