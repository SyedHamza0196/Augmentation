# find if there is any extra or missing image or label file in a specific folder before training
import os
import xml.etree.ElementTree as ET

labels_list = ['11 - Button Buttonholes',
               '31 - Crease Retention',
               '30 - Dry Process',
               '23 - Fabric Twisting',
               '21 - Fabric Flaw',
               '22 - Fabric Hole',
               '24 - Fabric Other',
               '25 - Fin Stain Oil',
               '35 - Finishing Others',
               '06 - Fullness',
               '09 - Hi Low',
               '29 - Holes',
               '14 - Loops',
               '04 - Needle Damage',
               '07 - Open Seam',
               '18 - Other Construction',
               '27 - Out of Shade Range',
               '39 - Pack Fold',
               '08 - Pleat',
               '40 - Pressing',
               '34 - Print Embroidery',
               '26 - Proc Splotch',
               '05 - Puckering',
               '02 - Raw Edge',
               '12 - Rivets Bar Tacks',
               '03 - Run Off',
               '32 - Seam Smoothness',
               '17 - Sew Stain Oil',
               '01 - Skipped Broken Stitch',
               '16 - Threads Loose',
               '15 - Threads Untrimmed',
               '13 - Twisted Leg']

# path = "/home/athar/MEGA/original_fixed"
# path = "/home/athar/MEGA/original"
# path = "/home/athar/MEGA/augmented/colorJitter"
# path = "/home/athar/MEGA/augmented/emboss"
path = "/home/athar/MEGA/augmented/randomBrightnessContrast"

folders = os.listdir(path)
for folder in folders:
    # folder = "Button-ButtonHoles"
    files = os.listdir(path+'/'+folder)

    labels = []
    images = []

    for file in files:
        # if file.split('.')[-1] == 'jpg':
        #     images.append(file)
        if file.split('.')[-1] == 'xml':
            labels.append(file)
        else:
            images.append(file)

    for file in labels:
        # if file.split('.')[-1] == 'xml':
        tree = ET.parse(path+'/'+folder+'/'+file)
        root = tree.getroot()

        for filename in root.iter('filename'):
            if filename.text not in images:
                print("xml jpg mismatch --> ", filename.text)
                print(path+'/'+folder+'/'+file)

        for label in root.iter('name'):
            if label.text not in labels_list:
                print("wrong label --> ", label.text)
                print(path+'/'+folder+'/'+file)
