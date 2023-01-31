from djitellopy import tello, Tello
import cv2
import time
import logging

#Tello.LOGGER.setLevel(logging.DEBUG)

me = tello.Tello()
me.connect()
# if me.connect(False):
#     print(me.get_battery())
# else:
#     print("no connect")

me.takeoff()
me.send_rc_control(0, 0, 0, -20)
time.sleep(1)
me.land()
# me.streamon()
#
# while True:
#     img = me.get_frame_read().frame
#     img = cv2.resize(img, (360, 240))#resize for faster
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)


