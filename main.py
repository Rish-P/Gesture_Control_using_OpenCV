import cv2
import mediapipe as mp
import hand_tracking_module as htm
import math
import osascript
import numpy as np


cap = cv2.VideoCapture(0)
#grab the hand detector class from hand tracking module
detector = htm.handDetector(detectionCon=0.7)


while True:
    _, frame = cap.read()
    img = detector.findHands(frame)
    lmlist = detector.findPosition(frame,draw=False)
    if len(lmlist)!=0:
        _,x4,y4 = lmlist[4]
        _,x8,y8 = lmlist[8]
        dist = math.sqrt(((x4-x8)**2) + ((y4-y8)**2))

        #draw 2 circles around thumb and index finger points
        cv2.circle(img, (x4,y4), 10, (255,0,0),cv2.FILLED)
        cv2.circle(img, (x8,y8), 10, (255,0,0),cv2.FILLED)

        cv2.line(img, (x4,y4),(x8,y8),(255,255,0),10)
        minVol = 0
        maxVol = 100
        vol = int(np.interp(dist,[40,330],[minVol,maxVol]))
        print(vol)
        setVol = "set volume output volume " + str(int(vol))
        osascript.osascript(setVol)

    cv2.imshow('FRAME', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
