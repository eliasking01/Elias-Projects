from djitellopy import Tello
import KeyPressModule as kp
import time
import cv2

me = Tello()
win = kp.init()
me.connect()
global img
me.streamon()

def getKeyboardInput():
	lr, fb, ud, yv = 0, 0, 0, 0
	speed = 100
	turnspeed = 100

	if kp.getKey("a"): lr = -speed
	elif kp.getKey("d"): lr = speed

	if kp.getKey("w"): fb = speed
	elif kp.getKey("s"): fb = -speed

	if kp.getKey("UP"): ud = speed
	elif kp.getKey("DOWN"): ud = -speed

	if kp.getKey("RIGHT"): yv = turnspeed
	elif kp.getKey("LEFT"): yv = -turnspeed

	if kp.getKey("f"): me.flip_forward()

	if kp.getKey("q"): me.land()
	if kp.getKey("e"): me.takeoff()

	if kp.getKey("ESCAPE"): me.emergency()

	if kp.getKey("SPACE"):
		cv2.imwrite(f"Resources/Images/{time.time()}.jpg", img)
		time.sleep(0.3)

	return [lr, fb, ud, yv]

def controls():
	vals = getKeyboardInput()
	me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

while True:
	controls()

	img = me.get_frame_read().frame
	img = cv2.resize(img,(1280, 720))
	cv2.imshow("Image", img)
	cv2.waitKey(1)
	battery = me.get_battery()
	kp.text(str(battery), win)
