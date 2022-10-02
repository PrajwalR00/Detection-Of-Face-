import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
# Display the output
cv2.imshow('Face Finder', img)
#cv2.imshow('face detect', gray)
cv2.waitKey()
