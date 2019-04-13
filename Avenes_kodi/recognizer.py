import cv2
import numpy as np
import os 
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "/home/pi/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

#None=id 0, Anne = id 1
names = ['None', 'Anne','Dairis'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 3,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        roi_color = img[y:y+h, x:x+w]
        
        if (confidence >=60 and confidence <=85):
            id = names[id]
            print(id)
        else:
            id = "unknown"
            print(id)
	
        cv2.putText(
                    img, 
                    str(id), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    img, 
                    str(confidence), 
                    (x+5,y+h-5), 
                    font, 
                    1, 
                    (255,255,0), 
                    1
                   )
        img_item = '/home/pi/opencv/build2/templates/static/images/person_'+ str(id) + '.jpg' #creates and image of the face and stores it 
        cv2.imwrite(img_item, roi_color)        
    
    cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff # ESC to exit
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup")
cam.release()
cv2.destroyAllWindows()
