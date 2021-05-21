import os
import csv
import pandas as pd
import time
import cv2


def convert(size, box):
	dw = 1./(size[0])
	dh = 1./(size[1])
	x = (box[0] + box[1])/2.0 - 1
	y = (box[2] + box[3])/2.0 - 1
	w = box[1] - box[0]
	h = box[3] - box[2]
	x = x*dw
	w = w*dw
	y = y*dh
	h = h*dh
	return (x,y,w,h)

gt_path='/home/macho/Desktop/Aletheia-AI/datasets/preprocess_and_validation/convert2Yolo/labels/annotations.txt'
images_path='/home/macho/Desktop/Aletheia-AI/datasets/preprocess_and_validation/convert2Yolo/images/'
save_label_path='/home/macho/Desktop/Aletheia-AI/datasets/preprocess_and_validation/convert2Yolo/labels/'
fd = open(gt_path, 'r')
lines = fd.readlines()

find_lbl=[]
for line in lines:
	line = line.strip().split(',')
	numboxes=int(line[1])#int((len(line)-1)/5)

	#print('image name-->',line[0])
	frame=cv2.imread(images_path+line[0])
	width = int(frame.shape[1])
	height= int(frame.shape[0])

	label_name=line[0].split('.')[0]
	#frame_=frame.copy()

	with open(save_label_path+label_name+'.txt','w') as fw:
		# print("is image mein ",line[0] ,"itny bounding box hain",line[1],"boxes -->")

		for i in range(2,numboxes*6,6):
			#print(i)
			x=int(line[i+1])
			y=int(line[i+2])
			w=int(line[i+3])#+x
			h=int(line[i+4])#+y
			# #print(line[i],line[i+1],line[i+2],line[i+3],line[i+4],line[i+5])
			b=[]
			b.append(x)
			b.append(w)
			b.append(y)
			b.append(h)
			find_lbl.append(line[i+5].strip())
			# cv2.rectangle(frame, (x,y), (w,h),(0,0,255), 2)
		#cv2.imshow('frame',frame)
		#cv2.waitKey(0)
			#frame_=frame.copy()
			#print(b)
			bb = convert((width,height), b)
		# 	label=''
			temp=line[i+5].strip()
			if temp=='person':
				label='0'
			# if temp=='null':
			# 	label='0'
			
			if temp not in find_lbl:
				print("garbar",temp,len(temp))
			fw.write('0 '+" ".join([str(a) for a in bb])+'\n')
	fw.close()
print(set(find_lbl))