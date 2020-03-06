import cv2
import numpy as np

def camera(frame1,frame2):
	hsvImage1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
	hsvImage2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
				
	lightGray = np.uint8([[[0,50,0]]])
	darkGray = np.uint8([[[179,50,255]]])

	mask1 = cv2.inRange(hsvImage1, lightGray, darkGray)
	mask2 = cv2.inRange(hsvImage2, lightGray, darkGray)

	result1 = cv2.bitwise_and(frame1, frame1, mask = mask1)
	result2 = cv2.bitwise_and(frame2, frame2, mask = mask2)

	grayImage1 = cv2.cvtColor(result1, cv2.COLOR_BGR2GRAY)
	grayImage2 = cv2.cvtColor(result2, cv2.COLOR_BGR2GRAY)

	edgedImage1 = cv2.Canny(grayImage1, 30, 200)
	edgedImage2 = cv2.Canny(grayImage2, 30, 200)

	contours1, hierarchy1 = cv2.findContours(edgedImage1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	contours2, hierarchy2 = cv2.findContours(edgedImage2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	cv2.drawContours(result1, contours1, -1, (0,255,0), 2)
	cv2.drawContours(result2, contours2, -1, (0,255,0), 2)

	#cv2.imshow('Contours1',result1)
	#cv2.imshow('Contours2',result2)

	trafficOnRoad1 = len(contours1)
	trafficOnRoad2 = len(contours2)
	
	trafficOnRoads = [trafficOnRoad1, trafficOnRoad2]
	
	return trafficOnRoads
