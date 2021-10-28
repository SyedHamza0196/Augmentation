import xml.etree.ElementTree as ET
import os

# path = "/home/athar/MEGA/original_fixed"
# path = '/home/athar/MEGA/original'
# path = '/home/athar/MEGA/augmented/colorJitter'
path = '/home/athar/MEGA/augmented/emboss'
# path = '/home/athar/MEGA/augmented/randomBrightnessContrast'

# folder = "train"
# folder = "test"

# folder = 'Button-Buttonholes'
# folder = 'CreaseRetention'
# folder = 'DryProcess'
# folder = 'FabricFlaw'
# folder = 'FabricHole'
# folder = 'FabricOther'
# folder = 'FabricTwisting'
# folder = 'FinishingOthers'
# folder = 'FinStain-Oil'
# folder = 'Fullness'
# folder = 'Hi-Low'
# folder = 'Holes'
# folder = 'Loops'
# folder = 'NeedleDamage'
# folder = 'OtherConstruction'
# folder = 'OutofShadeRange'
# folder = 'OpenSeam'
# folder = 'Pack-Fold'
# folder = 'Pleat'
# folder = 'Pressing'
# folder = 'Print-Embroidery'
# folder = 'ProcSplotch'
# folder = 'Puckering'
# folder = 'RawEdge'
# folder = 'Rivets-Bartacks'
# folder = 'RunOff'
# folder = 'SeamSmoothness'
# folder = 'SewStain-Oil'
# folder = "Skipped-BrokenStitch"
# folder = 'ThreadsLoose'
# folder = "ThreadsUntrimmed"
# folder = 'TwistedLeg'

# files = os.listdir(path+'/'+folder)

# for file in files:
#     if file.split('.')[-1] == 'xml':
#         tree = ET.parse(path+'/'+folder+'/'+file)
#         root = tree.getroot()

# for x in root.iter('name'):
# print(x.text)
# a = '11 - Button Buttonholes'
# a = '31 - Crease Retention'
# a = '30 - Dry Process'
# a = '21 - Fabric Flaw'
# a = "22 - Fabric Hole"
# a = '24 - Fabric Other'
# a = '23 - Fabric Twisting'
# a = '35 - Finishing Others'
# a = '25 - Fin Stain Oil'
# a = '06 - Fullness'
# a = '09 - Hi Low'
# a = '29 - Holes'
# a = '14 - Loops'
# a = '04 - Needle Damage'
# a = '18 - Other Construction'
# a = '27 - Out of Shade Range'
# a = '07 - Open Seam'
# a = '39 - Pack Fold'
# a = '08 - Pleat'
# a = '40 - Pressing'
# a = '34 - Print Embroidery'
# a = '26 - Proc Splotch'
# a = '05 - Puckering'
# a = '02 - Raw Edge'
# a = '12 - Rivets Bar tacks'
# a = '03 - Run Off'
# a = '32 - Seam Smoothness'
# a = '17 - Sew Stain Oil'
# a = '01 - Skipped Broken Stitch'
# a = '16 - Threads Loose'
# a = '15 - Threads Untrimmed'
# a = '13 - Twisted Leg'
# x.text = str(a)

# os.chdir(path+'/'+folder)
# tree.write(file)

folders = os.listdir(path)
count = 0
for folder in folders:
    files = os.listdir(path+'/'+folder)
    count = count + 1
    for file in files:
        if file.split('.')[-1] == 'xml':
            tree = ET.parse(path+'/'+folder+'/'+file)
            root = tree.getroot()

            for x in root.iter('name'):
                if x.text == 'Button Buttonholes':
                    print(x.text)
                    a = '11 - Button Buttonholes'
                    x.text = str(a)
                    # count = count + 1
                if x.text == 'Crease Retention':
                    print(x.text)
                    a = '31 - Crease Retention'
                    x.text = str(a)
                    # count = count + 1
                if x.text == 'Dry Process':
                    print(x.text)
                    a = '30 - Dry Process'
                    x.text = str(a)
                    # count = count + 1
                if x.text == 'Fabric Flaw':
                    print(x.text)
                    a = '21 - Fabric Flaw'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Fabric Hole":
                    print(x.text)
                    a = '22 - Fabric Hole'
                    x.text = str(a)
                    # count = count + 1
                if x.text == 'Fabric Other':
                    print(x.text)
                    a = '24 - Fabric Other'
                    x.text = str(a)
                    # count = count + 1
                if x.text == 'Fabric Twisting':
                    print(x.text)
                    a = '23 - Fabric Twisting'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Finishing Others":
                    print(x.text)
                    a = '35 - Finishing Others'
                    x.text = str(a)
                    # count = count + 1
                if x.text == 'Fin Stain Oil':
                    print(x.text)
                    a = '25 - Fin Stain Oil'
                    x.text = str(a)
                    # count = count + 1
                if x.text == 'Fullness':
                    print(x.text)
                    a = '06 - Fullness'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Hi Low":
                    print(x.text)
                    a = '09 - Hi Low'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Holes":
                    print(x.text)
                    a = '29 - Holes'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Loops":
                    print(x.text)
                    a = '14 - Loops'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Needle Damage":
                    print(x.text)
                    a = '04 - Needle Damage'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Other Construction":
                    print(x.text)
                    a = '18 - Other Construction'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Out of Shade Range":
                    print(x.text)
                    a = '27 - Out of Shade Range'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Open Seam":
                    print(x.text)
                    a = '07 - Open Seam'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Pack Fold":
                    print(x.text)
                    a = '39 - Pack Fold'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Pleat":
                    print(x.text)
                    a = '08 - Pleat'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Pressing":
                    print(x.text)
                    a = '40 - Pressing'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Print Embroidery":
                    print(x.text)
                    a = '34 - Print Embroidery'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Proc Splotch":
                    print(x.text)
                    a = '26 - Proc Splotch'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Puckering":
                    print(x.text)
                    a = '05 - Puckering'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Raw Edge":
                    print(x.text)
                    a = '02 - Raw Edge'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Rivets Bar tacks":
                    print(x.text)
                    a = '12 - Rivets Bar Tacks'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Run Off":
                    print(x.text)
                    a = '03 - Run Off'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Seam Smoothness":
                    print(x.text)
                    a = '32 - Seam Smoothness'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Sew Stain Oil":
                    print(x.text)
                    a = '17 - Sew Stain Oil'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Skipped Broken Stitch":
                    print(x.text)
                    a = '01 - Skipped Broken Stitch'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Threads Loose":
                    print(x.text)
                    a = '16 - Threads Loose'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Threads Untrimmed":
                    print(x.text)
                    a = '15 - Threads Untrimmed'
                    x.text = str(a)
                    # count = count + 1
                if x.text == "Twisted Leg":
                    print(x.text)
                    a = '13 - Twisted Leg'
                    x.text = str(a)
                    # count = count + 1
            os.chdir(path+'/'+folder)
            tree.write(file)
print(count)
