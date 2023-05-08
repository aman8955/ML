import numpy as np
import cv2
from time import sleep
fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0)
while True:
   flag, img =vid.read()
   if flag:
         img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         faces=fd.detectMultiScale(img_gray,  
            scalefactor=1.1,
            minNeighbors=5,
            minsize=(50,50)
         )
         np.random.seed(50)
         color =np.random.randint(0,255,(len(faces),3)).tolist()

         i=0
        

         for x,y,w,h in faces: 
            cv2.rectangle(
            img, pt1=(x,y),pt2=(x+w,y+h), color=(0,0,255),thickness=8
            )
            i+=1
         cv2.imshow('preview',img)
         key =cv2.waitKey(1)
         if key==ord('q'):
            break
   else:
      print('NO FRAMES')
      break
   sleep(0.1)
vid.release()
cv2.destroyAllWindows()
              

