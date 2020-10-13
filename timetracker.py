import cv2
import cvlib as cv
import time
import datetime
import sys


webcam = cv2.VideoCapture(0)
prevFace = True
startTime = time.time()
endTime = 0
lapsingTime = 0
totalTime = 0


if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()


    if not status:
        print("Could not read frame")
        exit()
    
    faces, confidence = cv.detect_face(frame)

    # if not prevFace and faces:
    #     startTime = time.time()
    #     prevFace = True

    # if prevFace and not faces:
    #     endTime = time.time()
    #     totalTime = totalTime + (endTime - startTime)
    #     prevFace = False
    
    if prevFace and faces:
        lapsingTime = time.time()
        totalTime = totalTime + (lapsingTime - startTime)

    if faces:
        startTime = time.time()
        prevFace = True
    else:
        prevFace = False

    for face in faces:
        startX = face[0]
        startY = face[1]
        endX = face[2]
        endY = face[3]

        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.putText(frame, str(totalTime), (startX,startY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
        

    cv2.imshow("Webcam face detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()



