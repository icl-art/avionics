import cv2
from cv2 import dnn_superres
import time

start = time.time()

print ("Getting Frame")

cap = cv2.VideoCapture("TreesIn.mp4")

_, frame = cap.read()

#frame = cv2.imread("frame1.png")

#cv2.imshow("original", frame)
#time.sleep(5)

## EDSR does not work
print ("Setting up model")
sr = dnn_superres.DnnSuperResImpl_create()
sr.readModel("EDSR_x2.pb")    
sr.setModel("edsr", 2)

print("Upscaling")
upscaled = sr.upsample(frame)

#cv2.imshow("upscaled", upscaled)

duration = time.time() - start

print(duration)

cv2.imwrite("./EDSR_x2.png", upscaled)
