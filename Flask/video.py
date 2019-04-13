import cv2
from face_rec import Recognizer
face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
   
def Camera():
	while True:
		ret, img = cam.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
		faces = face_cascade.detectMultiScale(
			gray,
			scaleFactor = 1.3,
			minNeighbors = 3,
			minSize = (int(minW), int(minH)),
		)

		for(x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
	
	return cv2.imencode('.jpeg', img)[1].tobytes()
