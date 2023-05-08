import cv2
import matplotlib.pyplot as plt
vid=cv2.VideoCapture(0)
while True:
   flag, img =vid.read()
   if flag:
      #processing code
      img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      faces=fd.detectmultiscale(img_gray,1.1,5)
      # th, img_bw = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY_INV )
      # x,y,w,h = (250,200,100,100)
      # img_cropped = img[y:y+h,x:x+w,:]     

      cv2.rectangle(
         img, pt1=(x,y),pt2=(x+w,y+h), color=(0,0,255),
         thickness=8)
      
     
      cv2.imshow('preview',img)
      key =cv2.waitKey(1)
      if key==ord('q'):
        break
   else:
      print('NO FRAMES')
      break
cv2.destroyAllWindows()
cv2.waitKey(1)              
vid.release()
del vid