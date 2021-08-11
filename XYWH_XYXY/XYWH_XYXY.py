import os
import cv2

images = os.listdir("images/val") #mkdir images folder with code file
labels = os.listdir("labels/val") #mkdir labels folder with code file

#WRITE DENORMALIZED
if not os.path.exists('result/val'): #mkdir result with code file if not present
    os.mkdir('result/val')

for image in images:
    img = cv2.imread("images/val/"+image)
    label = image.replace(".jpg",".txt")

    dh, dw, _ = img.shape
    with open("labels/val/"+label, 'r') as fr:
        lines = fr.readlines()
        with open("result/val/"+label, 'w') as fw:
            for line in lines:
                # print(line.split())
                id, xc, yc, w, h = line.split(' ')
                # x1 = float((float(x) - float(w)) / 2) * dw 
                # print(type(x1))
                x1 = str(int((float(xc) - float(w) / 2) * dw))
                y1 = str(int((float(yc) - float(h) / 2) * dh))
                # x2 = str(int((float(xc) + float(w) / 2) * dw))
                # y2 = str(int((float(yc) + float(h) / 2) * dh))
                w = str(int(float(w) * dw))
                h = str(int(float(h) * dh))

                # fw.write(id+" "+x1+" "+y1+" "+x2+" "+y2+"\n")
                fw.write(str(id)+" "+x1+" "+y1+" "+w+" "+h+"\n")

