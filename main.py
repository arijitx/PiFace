import cv2
import numpy as np 
import os
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer=cv2.face.createLBPHFaceRecognizer()



#Loading each image and cropping the face preparing the dataset

# for filename in os.listdir('Dataset'):
# 	im=cv2.imread('Dataset/'+filename,0)
# 	print filename
# 	faces = faceCascade.detectMultiScale(im, 1.3, 5)
# 	for (x,y,w,h) in faces:
# 		cv2.imwrite('Dataset/'+filename,im[y:y+h, x:x+w])
	


images=[]
labels=[]
for filename in os.listdir('Dataset'):
	im=cv2.imread('Dataset/'+filename,0)
	images.append(im)
	labels.append(int(filename.split('.')[0][0]))
	#print filename


names_file=open('labels.txt')
names=names_file.read().split('\n')


recognizer.train(images,np.array(labels))
print 'Training Done . . . '

font = cv2.FONT_HERSHEY_SIMPLEX
cap=cv2.VideoCapture(1)
lastRes=''
count=0

while(1):
	_,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, 1.3, 5)
	count+=1

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		if count>20:
			res=names[recognizer.predict(gray[y:y+h, x:x+w])-1]
			if res!=lastRes :
				lastRes=res
				print lastRes
				ser.write(lastRes)
			count=0
		break

	
	
	cv2.imshow('frame',frame)
	k = 0xFF & cv2.waitKey(10)
	if k == 27:
		break
cap.release()
ser.close()
cv2.destroyAllWindows()