import xml.etree.ElementTree as ET
import os

# path = '/home/athar/MEGA/original'
# path = '/home/athar/MEGA/augmented/colorJitter'
# path = '/home/athar/MEGA/augmented/emboss'
path = '/home/athar/MEGA/augmented/randomBrightnessContrast'

folders = os.listdir(path)
for folder in folders:
    files = os.listdir(path+'/'+folder)
    for file in files:
        if file.split('.')[-1] == 'xml':
            tree = ET.parse(path+'/'+folder+'/'+file)
            root = tree.getroot()

            for x in root.iter('filename'):
                print(x.text)
                a = file.split('.')[0]+'.jpg'
                print(a)
                x.text = str(a)

            os.chdir(path+'/'+folder)
            tree.write(file)
