font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

#None=id 0, Anne = id 1
names = ['None', 'Anne','Dairis','Ernests'] 

# Initialize and start realtime video capture
cap = cv2.VideoCapture(0)
cap.set(3, 840) # widht
cap.set(4, 480) # height

# Define min window size to be recognized as a face
minW = 0.1*cap.get(3)
minH = 0.1*cap.get(4)

while True:
    ret, img =cap.read()
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
            confidence = "  {0}%".format(round(confidence))        
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(confidence))        
        color= (255, 255, 255)
        stroke= 2

        cv2.putText(
                    img, 
                    str(id), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    color, 
                    stroke
                   )
        cv2.putText(
                    img, 
                    str(confidence), 
                    (x+5,y+h-5), 
                    font, 
                    1, 
                    (255,255,0), 
                    stroke
                   )
        img_item = '/home/pi/share/person_'+ str(id) + '.jpg' #creates and image of the face and stores it
        cv2.imwrite(img_item, roi_color)        
    
    cv2.imshow('camera',img)
    k = cv2.waitKey(20) & 0xff # ESC to exit
    if k == 27:
        break

# Do a bit of cleanup
print("[INFO] Izsledz programmu")
cap.release()
cv2.destroyAllWindows()
