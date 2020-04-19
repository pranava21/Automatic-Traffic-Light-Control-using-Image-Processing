import cv2
import numpy as np

def getTrafficDensityFromImages(image):
    cropped = image[0:768, 615:980]
    
    #gamma correction
    image = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,15)
    img = dst/255
    img = cv2.pow(img, 2) 
    new_image = np.uint8(img*255)

    #Mask 1
    kernel = np.ones((5, 5), np.uint8)
    dilation_image = cv2.dilate(new_image, kernel, iterations=2)
    hsv_im = cv2.cvtColor(dilation_image, cv2.COLOR_RGB2HSV)
    
    light_gray = np.uint8([[[0, 3, 50]]])
    dark_gray = np.uint8([[[179, 50, 255]]])
    
    mask = cv2.inRange(hsv_im, light_gray, dark_gray)
    result = cv2.bitwise_and(image, image, mask=mask)

    #mask 2
    hsv_im2 = cv2.cvtColor(dilation_image, cv2.COLOR_BGR2HSV)
    
    light_green = np.uint8([[[80, 40, 30]]])
    dark_green = np.uint8([[[138, 100, 78]]])
    
    mask = cv2.inRange(hsv_im2, light_green, dark_green)
    r = cv2.bitwise_not(dilation_image, dilation_image,  mask=mask)

    #image subtraction
    op = cv2.subtract(result, r)
  
    #edge detection and finding area
    gray = cv2.cvtColor(op, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200) #(img, lower, upper) threshold values
    
    contours, hierarchy = cv2.findContours(edged,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for c in contours:
        area = cv2.contourArea(c)
        areas = np.append(areas, area)

    return int(np.sum(areas))
