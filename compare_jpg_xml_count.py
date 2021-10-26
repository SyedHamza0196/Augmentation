# find if there is any extra or missing image or label file in a specific folder before training
import os

path = "/home/athar/MEGA/taggedData/Fabric Other"
files = os.listdir(path)

labels = []
images = []

for file in files:
    if file.split('.')[-1] == 'jpg':
        images.append(file.split('.')[0])
    if file.split('.')[-1] == 'xml':
        labels.append(file.split('.')[0])

if len(labels) == len(images):
    print("number of files is EVEN")
    for label in labels:
        if label not in images:
            print(label+' label is extra')

if len(labels) > len(images):
    print("len(images) is greater")
    for label in labels:
        if label not in images:
            print(label+' label is extra')
if len(images) > len(labels):
    print("len(labels) is greater")
    for image in images:
        if image not in labels:
            print(image+' image is extra')
