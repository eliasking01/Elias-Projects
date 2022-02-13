### TESTED IN FEDORA LINUX ###

import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from subprocess import call

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(maxHands = 1, detectionCon = 0.8)

while True:
	success, img = cap.read()
	img = detector.findHands(img)
	lmList = detector.findPosition(img, draw = False)

	if len(lmList) != 0:
		x1, y1 = lmList[4][1], lmList[4][2]
		x2, y2 = lmList[8][1], lmList[8][2]
		x3, y3 = lmList[12][1], lmList[12][2]
		cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

		def blackLines():
			cv2.circle(img, (x1, y1), 15, (0, 0, 0), cv2.FILLED)
			cv2.circle(img, (x2, y2), 15, (0, 0, 0), cv2.FILLED)
			cv2.circle(img, (cx, cy), 15, (0, 0, 0), cv2.FILLED)
			cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 3)

		cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
		cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
		cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
		cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

		length = math.hypot(x2 - x1, y2 - y1) - 50
		length2 = math.hypot(x3 - x2, y3 - y2)
		volume = int(length)

		free = False

		if length < 0:
			blackLines()
			volume = 0
		elif length > 100:
			blackLines()
			volume = 100

		if free == False:
			if length < 60 and length > 40:
				volume = 50
			elif length <= 90 and length > 60:
				volume = 75
			elif length < 40 and length >= 10:
				volume = 25

			if length < 10:
				blackLines()
				volume = 0
			elif length > 90:
				blackLines()
				volume = 100
		else:
			if length < 0:
				blackLines()
				volume = 0
			elif length > 100:
				blackLines()
				volume = 100

		if length2 > 100:
			call(["pactl", "set-sink-volume", "0", str(volume) + "%"])
			cv2.putText(img, f"Volume: {volume}%", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
			print("Volume:", volume)
		else:
			blackLines()

	cv2.imshow("Img", img)
	cv2.waitKey(1)
