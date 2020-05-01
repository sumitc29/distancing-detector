#camera.py
# import the necessary packages
import cv2
# defining face detector
#face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
classifier = cv2.CascadeClassifier('temp.xml')
ds_factor=0.6


import cv2
from datetime import datetime

class VideoCamera(object):
	def __init__(self):
		#capturing video
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		#releasing camera
		self.video.release()
	
	def get_frame(self):
	       #extracting frames
		ret, img = self.video.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
		faces = classifier.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=5,
		    minSize=(30, 30))

		font                   = cv2.FONT_HERSHEY_SIMPLEX
		bottomLeftCornerOfText = (10,500)
		fontScale              = 0.5
		fontColor              = (255,255,255)
		lineType               = 2


		for (x, y, w, h) in faces:
		    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		    cv2.putText(img,'Hello World!', 
		    bottomLeftCornerOfText, 
		    font, 
		    fontScale,
		    fontColor,
		    lineType)

		x1=[]
		y1=[]
		w1=[]
		h1=[]
		for (x,y,w,h) in faces:
			x1.append(x)
			y1.append(y)
			w1.append(w)
			h1.append(h)
		
		# Put current DateTime on each frame
		font = cv2.FONT_HERSHEY_SIMPLEX

		if len(x1) != 0:

			sttr=' '
			if len(x1) > 1:
				diff = abs((x1[0]+w1[0]) - (x1[1]+w1[1]))
				if diff>100:
					sttr = sttr+"Thanks for maintaining distancing "
					cv2.putText(img,sttr,(10,30), font, 1,(0,255,0),2,cv2.LINE_AA)
				else:
					sttr = sttr+" please maintain distancing "
					cv2.putText(img,sttr,(10,30), font, 1,(0,0,255),2,cv2.LINE_AA)
		else:
			cv2.putText(img,'not detected',(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)


		# encode OpenCV raw frame to jpg and displaying it
		ret, jpeg = cv2.imencode('.jpg', img)
		return jpeg.tobytes()
