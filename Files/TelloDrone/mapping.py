from djitellopy import Tello
import KeyPressModule as kp
import time
import cv2
import numpy as np
import math

### PARAMETERS ###
fspeed = 117/5 # Forward speed in cm/s (30cm/s)
aspeed = 360/5 # Angular speed degrees/s (100d/s)
interval = 0.25

dinterval = fspeed * interval
ainterval = aspeed * interval
##################
x, y = 500, 500
a = 0
yaw = 0

me = Tello()
win = kp.init()
me.connect()
global img
me.streamon()

points = [(0, 0), (0, 0)]

def getKeyboardInput():
	global x, y, yaw, a
	lr, fb, ud, yv = 0, 0, 0, 0
	speed = 30
	aspeed = 100
	d = 0

	if kp.getKey("a"): 
		lr = -speed
		d = dinterval
		a = -180

	elif kp.getKey("d"): 
		lr = speed
		d = -dinterval
		a = 180

	if kp.getKey("w"): 
		fb = speed
		d = dinterval
		a = 270

	elif kp.getKey("s"): 
		fb = -speed
		d = -dinterval
		a = -90

	if kp.getKey("UP"): 
		ud = speed
	elif kp.getKey("DOWN"): 
		ud = -speed

	if kp.getKey("RIGHT"): 
		yv = aspeed
		yaw += ainterval

	elif kp.getKey("LEFT"): 
		yv = -aspeed
		yaw -= ainterval

	if kp.getKey("q"): me.land()
	if kp.getKey("e"): me.takeoff()

	if kp.getKey("ESCAPE"): me.emergency()

	if kp.getKey("SPACE"):
		cv2.imwrite(f"Resources/Images/{time.time()}.jpg", img)
		time.sleep(0.3)

	time.sleep(interval)
	a += yaw
	x += int(d*math.cos(math.radians(a)))
	y += int(d*math.sin(math.radians(a)))

	return [lr, fb, ud, yv, x, y]

def controls():
	vals = getKeyboardInput()
	me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
	return vals

def drawPoints(img1, points):
	for point in points:
		cv2.circle(img1, point, 5, (0 , 0, 255), cv2.FILLED)

	cv2.circle(img1, points[-1], 8, (0 , 255, 0), cv2.FILLED)
	cv2.putText(img1, f"({(points[-1][0] - 500) / 100}, {(points[-1][1] - 500) / 100})m",
				(points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,
				(255, 0, 255), 1)

while True:
	vals = controls()

	img = me.get_frame_read().frame
	img = cv2.resize(img,(1280, 720))
	cv2.imshow("Image", img)
	battery = me.get_battery()
	kp.text(str(battery), win)

	img1 = np.zeros((1000, 1000, 3), np.uint8)
	if (points[-1][0] != vals[4] or points[-1][1] != vals[5]):
		points.append((vals[4], vals[5]))
	drawPoints(img1, points)
	cv2.imshow("Output", img1)
	cv2.waitKey(1)
