import cv2
import DataTransmition as dt
import time

IS = dt.ImageSender("192.168.1.2", 40000, (320, 320))

while True:
	cam = cv2.VideoCapture("../../../video_test.webm")
	ok = True
	start = time.time()
	while ok:
		fps = 1/(time.time() - start)
		start = time.time()
		print("              \rFPS:", fps, end='\r')
		ok, img = cam.read()
		if ok: IS.send(img)
		time.sleep(1/240)
	cam.release()
