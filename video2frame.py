import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/66401/Desktop/video_test_0000001.webm")
write_path="C:/Users/66401/Desktop/video_test_0000001/"
frame_interval=5
c=0
now=0
rval=cap.isOpened()

while rval:
	ret,frame=cap.read()
	if rval and c%frame_interval==0:
		now+=1
		frame=cv2.resize(frame,(320,180))
		cv2.imshow("cap",frame)
		cv2.imwrite(write_path+"img_"+str(now).zfill(5)+'.jpg',frame)
		if cv2.waitKey(100)&0xFF==ord('q'):
			break
	c+=1
cap.release()
cv2.destroyAllWindows()