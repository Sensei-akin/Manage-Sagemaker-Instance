import imutils
from skimage.filters import threshold_local
import cv2,base64,os, argparse
import numpy as np
import random
import pytesseract
from skimage import measure
import re,datetime,json

# Reading the image 
path = '/Users/akinwande.komolafe/Documents/streamlit-projects/passportpage.jpg'
image = cv2.imread(path)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img =image
# Extraction of text from image
# text = pytesseract.image_to_string(image)


# perform a image cleaning to enhance constrast and borders
def cleanImage(image, stage = 0):
    V = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # applying topHat/blackHat operations
    topHat = cv2.morphologyEx(V, cv2.MORPH_TOPHAT, kernel)
    blackHat = cv2.morphologyEx(V, cv2.MORPH_BLACKHAT, kernel)
    # add and subtract between morphological operations
    add = cv2.add(V, topHat)
    subtract = cv2.subtract(add, blackHat)
    if (stage == 1):
        return subtract
    T = threshold_local(subtract, 29, offset=35, method="gaussian", mode="mirror")
    thresh = (subtract > T).astype("uint8") * 255
    if (stage == 2):
        return thresh
    # invert image 
    thresh = cv2.bitwise_not(thresh)
    return thresh


cv2.imshow('result',cleanImage(image))
cv2.waitKey(0)
# ## detecting characters

# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img)

# for b in boxes.splitlines():
#     b = b.split(' ')
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4]) 
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),3)
# cv2.imshow('result',img)
# cv2.waitKey(0)