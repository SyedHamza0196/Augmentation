import time
import cv2
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import glob
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import math

video_path='/home/hamza/Desktop/tmp_work/demo/box_.mp4'
#gt_file='/home/sharf-e-hayder/Videos/raw videos/people_lables.txt'
cap = cv2.VideoCapture(video_path)
w=int(cap.get(3))
h=int(cap.get(4))
print(h,w)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('LuckyCementFactory.mp4',fourcc,24,(w,h))#int(cap.get(5)),(w,h))


dic={}
d1 = defaultdict(list)

# fd = open(gt_file, 'r')
# lines = fd.readlines()

# number_line=int(len(lines))

# for line in lines:
# 	line = line.strip().split(',')
# 	numboxes=int(float(line[1]))

# 	for i in range(2,numboxes*5,5):
# 		tracks=[]
# 		tracks.append([line[i],line[i+1],line[i+2],line[i+3],line[i+4]])
# 		temp_frame=(line[0].replace("frame",""))
# 		d1[int(temp_frame)].append(tracks)
		#print(tracks)
	

	
#print(len(d1[0]))0,4,965,680,239,203,523,578,206,334,297,630,89,187,251,627,51,177
# counter=7
# t_c=0
# t_c_1=0
count=0
while(1):
	ret,frame = cap.read()
	if ret==False:
		break
	
	# imgplot = plt.imshow(frame)
	# plt.show()


	over = frame.copy()
	over=cv2.rectangle(over,(0,0), (250,50), (cv2.COLORMAP_OCEAN), -1)
	frame = cv2.addWeighted(over,0.4,frame, 0.6, 0)
	if cap.get(1)>34:
		count=1
	if cap.get(1)>115:
		count=2
	if cap.get(1)>153:
		count=3
	if cap.get(1)>202:
		count=4
	if cap.get(1)>243:
		count=5
	if cap.get(1)>297:
		count=6
	if cap.get(1)>342:
		count=7
	if cap.get(1)>442:
		count=8
	if cap.get(1)>497:
		count=9
	if cap.get(1)>569:
		count=10
	if cap.get(1)>663:
		count=11
	if cap.get(1)>761:
		count=12
	if cap.get(1)>848:
		count=13
	if cap.get(1)>891:
		count=14
	if cap.get(1)>939:
		count=15
	if cap.get(1)>990:
		count=16
	if cap.get(1)>1023:
		count=17
	if cap.get(1)>1068:
		count=18
	if cap.get(1)>1126:
		count=19
	if cap.get(1)>1219:
		count=20
	if cap.get(1)>1294:
		count=21
	if cap.get(1)>1342:
		count=22
	if cap.get(1)>1389:
		count=23
	if cap.get(1)>1429:
		count=24
	if cap.get(1)>1493:
		count=25
	if cap.get(1)>1528:
		count=26
	if cap.get(1)>1580:
		count=27
	if cap.get(1)>1618:
		count=28
	if cap.get(1)>1659:
		count=29
	if cap.get(1)>1697:
		count=30
	if cap.get(1)>1744:
		count=31
	if cap.get(1)>1784:
		count=32
	if cap.get(1)>1842:
		count=33
	if cap.get(1)>1875:
		count=34
	if cap.get(1)>1931:
		count=35
	# if cap.get(1)>2003:
	# 	count=36
	# if cap.get(1)>2034:
	# 	count=37
	# if cap.get(1)>2090:
	# 	count=38
	# if cap.get(1)>2122:
	# 	count=39
	# if cap.get(1)>2167:
	# 	count=40
	# if cap.get(1)>2223:
	# 	count=41
	# if cap.get(1)>2258:
	# 	count=42
	# if cap.get(1)>2311:
	# 	count=43
	# if cap.get(1)>2357:
	# 	count=44
	# if cap.get(1)>2406:
	# 	count=45

	cv2.putText(frame," Bag count= "+(str(count)),(10,30),0,0.7, (255,255,255),2)
	# #cv2.putText(frame,"Vehicles at fuel area 1 : suzuki cultus white",(10,50),0,0.7, (255,255,255),2)
	#cv2.putText(frame,"Vehicles at fuel area 2 : ",(10,70),0,0.7, (255,255,255),2)

	# #cv2.putText(frame,"Vehicles at fuel area 3 : toyota corolla white",(10,90),0,0.7, (255,255,255),2)
	
	# temp= int(cap.get(1))
	# temp=temp/20
	# temp=round(temp)
	
	#  	t_c_1+=1
	#  	temp_1=t_c_1 
	#  	temp_1=temp_1/20
	# 	temp_1=round(temp_1)
	# 	cv2.putText(frame,"Vehicles at fuel area 3 : toyota corolla white (stay time: 00:00:"+str(temp_1)+')',(10,90),0,0.7, (255,255,255),2)
	# else:
	# 	cv2.putText(frame,"Vehicles at fuel area 3 :",(10,90),0,0.7, (255,255,255),2)



	# cv2.putText(frame,"Vehicles at fuel area 1 : suzuki cultus white (stay time: 00:00:"+str(temp)+')',(10,50),0,0.7, (255,255,255),2)



	# if cap.get(1)>650:
	# 	t_c+=1
	# 	temp= t_c
	# 	temp=temp/20
	# 	temp=round(temp)

	# 	cv2.putText(frame,"toyota corolla white (stay time: 00:00:"+str(temp)+')',(850,90),0,0.7, (255,255,255),2)


	

	# #if int(cap.get(1))%50==0:/mnt/565CA5115CA4ED45/clients/cement_lucky/cement717.mp4
	# #	counter+=1
	# if int(cap.get(1))==200:
	# 	counter=14

	# if int(cap.get(1))==300:
	# 	counter=16
	# if int(cap.get(1))==400:
	# 	counter=19

	# if int(cap.get(1))==600:
	# 	counter=21
	# if int(cap.get(1))==700:
	# 	counter=25
	# if int(cap.get(1))==900:
	# 	counter=28
	# if int(cap.get(1))==1000:
	# 	counter=32
	# #if counter<33:
	# cv2.putText(frame,str(counter),(300,30),0,0.7, (255,255,255),2)



		





	# over_1 = frame.copy()
	# over_1=cv2.rectangle(over_1,(85,650),(960,1080),(150,0,150), -1)
	# frame = cv2.addWeighted(over_1,0.4,frame, 0.6, 0)



	# cv2.line(frame,(462,372),(768,372),(0,0,255),2)
	# cv2.line(frame,(768,372),(240,818),(0,0,255),2)
	# cv2.line(frame,(240,818),(4,710),(0,0,255),2)
	# cv2.line(frame,(4,710),(462,372),(0,0,255),2)
	# cv2.putText(frame,"fuel area 1",(319,579),0,0.8, (0,255,0),2)


	# cv2.line(frame,(1039,374),(1235,349),(0,0,255),2)
	# cv2.line(frame,(1235,349),(1123,851),(0,0,255),2)
	# cv2.line(frame,(1123,851),(779,852),(0,0,255),2)
	# cv2.line(frame,(779,852),(1039,374),(0,0,255),2)
	# cv2.putText(frame,"fuel area 2",(995,600),0,0.8, (0,255,0),2)


	# cv2.line(frame,(1397,318),(1723,335),(0,0,255),2)
	# cv2.line(frame,(1723,335),(1910,787),(0,0,255),2)
	# cv2.line(frame,(1910,787),(1425,807),(0,0,255),2)
	# cv2.line(frame,(1425,807),(1397,318),(0,0,255),2)
	# cv2.putText(frame,"fuel area 3",(1600,580),0,0.8, (0,255,0),2)

	# out.write(frame)




	

	#cv2.putText(frame,'FUEL AREA',(450,850),0,1, (255,255,0),2)

	#cv2.putText(frame,'License Plate Number : TAE 487',(10,30),0,1, (255,255,0),2)
	#cv2.putText(frame,'Tyres Count           : 10',(10,60),0,1, (255,255,0),2)
	
#	if int(cap.get(1))>1132:
#		break
	#cv2.putText(frame,"OCR Results : ",(10,30),0,0.7, (255,0,0),2)
	#print(cap.get(1))
	# if d1[int(cap.get(1))]:
	# 	#sprint("hh")
	# 	temp=d1[int(cap.get(1))]

	# 	#cv2.putText(frame,"cement bags count : "+str(len(temp)),(10,30),0,0.7, (255,0,0),2)
	# 	for i in range(len(temp)):
	# 		#print(temp)
	# 		x=int(temp[i][0][0])
	# 		y=int(temp[i][0][1])
	# 		w=int(temp[i][0][2])
	# 		h=int(temp[i][0][3])
	# 		temp_label=temp[i][0][4]
	# 		if temp_label=="face mask" or "no face mask":
	# 			cv2.putText(frame, str(temp_label),(x+w,y+h-10),0,1, (0,255,255),2)
	# 		else:
	# 			cv2.putText(frame, str(temp_label),(x,y-10),0,1, (0,255,255),2)
	# 		cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255), 2)

			
			# out.write(frame)
			# cv2.imshow('frame',frame)
			# if cv2.waitKey(1) & 0xFF == ord('q'):
			# 		break
			
			#if i==0:
			#	value=170
			#else:
			#	value=value+120	
		
	#		cv2.putText(frame,str(temp_label),(value,30),0,0.7, (255,255,255),2)
			
			# elif temp_label=='rickshaw':
			# 	cv2.putText(frame, str(temp_label),(x-10,y-10),0,0.8, (255,255,255),2)
			# 	cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0), 2)
			# else:
			# 	cv2.putText(frame, str(temp_label),(x-10,y-10),0,0.8, (255,255,255),2)
			# 	cv2.rectangle(frame, (x,y), (x+w,y+h),(255,255,0), 2)
			# start_point = (94,452)	
			# end_point = (528,276)
			# color = (0, 255, 0)
			# thickness = 3
			# frame = cv2.line(frame, start_point, end_point, color, thickness)
		#cv2.imshow(window_name, image)	



	out.write(frame)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	



	


cap.release()
out.release()

