
### This script detects if you run, jump, the speed/height when you run/jump, and the side of the camera you are on.

import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture(2)
pTime = 0
detector = pm.poseDetector()

speed = 0
speed1 = 0
leftStart = False
rightStart = False

tend = 0
tstart = 0

side = "none"

timer = False

jump1 = 0
jump2 = 0

j = True

jHeight = 0

while True:
    jump = False

    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw = False)

    img = cv2.resize(img, (1920, 1080))

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if len(lmList) != 0:
        palmDistanceY = lmList[16][2] - lmList[15][2]
        kneeDistanceY = lmList[26][2] - lmList[25][2]

        # LEFT
        if leftStart:
            if palmDistanceY < -35 and kneeDistanceY > 5:
                leftStart = False
                tend = time.time()
                speed = tend - tstart
        elif not rightStart:
            if palmDistanceY > 35 and kneeDistanceY < -5:
                tstart = time.time()
                leftStart = True

        # RIGHT
        if rightStart:
            if palmDistanceY > 35 and kneeDistanceY < -5:
                rightStart = False
                tend = time.time()
                speed1 = tend - tstart
        elif not leftStart:
            if palmDistanceY < -35 and kneeDistanceY > 5:
                tstart = time.time()
                rightStart = True

        speed = (speed + speed1) / 2

        # INACTIVE
        if time.time() - tstart > 1:
            speed = 0

        if speed <= 1 and speed != 0:
            speed = 1 - speed
        else:
            speed = 0

        bodyCenterX = (lmList[24][1] + lmList[23][1]) / 2
        bodyCenterY = (lmList[24][2] + lmList[23][2]) / 2

        if bodyCenterX >= 0 and bodyCenterX < (width / 3):
            side = "right"

        if bodyCenterX >= (width / 3) and bodyCenterX < (width / 3) * 2:
            side = "middle"

        if bodyCenterX >= (width / 3) * 2:
            side = "left"

        if not timer:
            cstart = time.time()
            timer = True
            jump1 = bodyCenterY

        if time.time() - cstart > 0.1:
            jump2 = bodyCenterY

            if time.time() - cstart > 0.5:
                timer = False
                jump = False
                j = True
                jHeight = 0
            else:
                if j:
                    if (jump2 - jump1) + jump1 <= jump1 - 35:
                        jump = True
                        j = False
                        jHeight = jump2 - jump1
                        jHeight = 0 - jHeight

    else:
        side = "none"
        speed = 0
        jHeight = 0

    print("Speed:", speed)
    print("Jump:", str(jump) + ",", "Height:", jHeight)
    print("Side:", side)
