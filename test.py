from picamera import PiCamera
import time

cam = PiCamera()
cam.vflip = True



cam.start_preview()
time.sleep(2)

cam.capture("test.jpg")

