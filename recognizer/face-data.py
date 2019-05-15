import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height
face_detector = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press enter ==>  ')
print("\n [INFO] Look the camera and wait ...")

# Initialize individual sampling face count
count = 0

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        
        cv2.imwrite("/home/pi/dataset/User." + str(face_id) + '.' +  
                    str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 15: # Take 15 face sample and stop video
         break

# Do a bit of cleanup
print("[INFO] Izsledz programmu")
cap.release()
cv2.destroyAllWindows()
