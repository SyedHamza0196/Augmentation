import os
import os.path
from bs4 import BeautifulSoup
import cv2

address = '/home/athar/Desktop/DataPilot/Projects/Levis/fabricFaultDetection/Teas/Tops/Button-Buttonholes/'
files = os.listdir(address)

for file in files:
    if file.split('.')[-1] == 'jpg':
        label = file.split('.')[0]+'.xml'
        os.chdir(address)
        if os.path.isfile(label):
            # print(address+file)
            image = cv2.imread(file)
            with open(address+'/'+label,'r') as f:
                data = f.read()
                data2 = BeautifulSoup(data,'xml')

                xmin = int(data2.find('xmin').string)
                ymin = int(data2.find('ymin').string)
                xmax = int(data2.find('xmax').string)
                ymax = int(data2.find('ymax').string)

                start_point = (xmin,ymin)
                end_point = (xmax,ymax)
                image = cv2.rectangle(image, start_point, end_point, (0,255,0), 2)
                cv2.imshow('labeled image', image)
                cv2.waitKey(0)