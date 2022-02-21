import cv2
import numpy as np 
import time

def CnC(t):

	cap = cv2.VideoCapture(0)
	face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

	timeout = t #seconds after camera will close
	timeout_start = time.time()

	while time.time() < timeout_start + timeout:
		ret,frame = cap.read()

		gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		if ret == False:
			continue

		faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
		if len(faces) == 0:
			continue

		for face in faces:
			x,y,w,h = face

			offset_x = 80
			offset_y = 120

			face_offset = frame[y-offset_y:y+h+offset_y,x-offset_x:x+w+offset_x]
			
			width = 120
			height = 160
			dim = (width, height)

			face_selection = cv2.resize(face_offset,dim)

			cv2.imshow("Face", face_selection)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


		cv2.imshow("faces",frame)
		key_pressed = cv2.waitKey(1) & 0xFF
		if key_pressed == ord('q'):
			break

	SentDataFolder = '/home/jacksparrow/Desktop/Final_Fusion/Data Folder/Sent Image/'
	cv2.imwrite(SentDataFolder + "TempImg.jpg",face_selection)
	
#	time.sleep(2)


	cap.release()
	cv2.destroyAllWindows()
