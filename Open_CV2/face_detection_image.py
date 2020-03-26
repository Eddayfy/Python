#!/usr/bin/python3
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('./.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Read the input image
image = input("Enter the Image URL: ")
img = cv2.imread(image)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
