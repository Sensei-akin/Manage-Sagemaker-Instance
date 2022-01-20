import pytesseract
import cv2
# Reading the image 
image = cv2.imread('/Users/akinwande.komolafe/Downloads/Emena/letter.jpg')
# Extraction of text from image
text = pytesseract.image_to_string(image)
print(text)