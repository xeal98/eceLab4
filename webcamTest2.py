import cv2
for i in range(0, 10):
   webcam = cv2.VideoCapture(i)
   if webcam.isOpened():
       print(f"Camera found at index {i}")
       break