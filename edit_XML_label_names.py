import xml.etree.ElementTree as ET
import os

# path = '/home/athar/MEGA/taggedData'
# path = '/home/athar/MEGA/augmented/colorJitter'
# path = '/home/athar/MEGA/augmented/emboss'
path = '/home/athar/MEGA/augmented/randomBrightnessContrast'
folder = 'Button-Buttonholes'
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
files = os.listdir(path+'/'+folder)

for file in files:
    if file.split('.')[-1] == 'xml':
        tree = ET.parse(path+'/'+folder+'/'+file)
        root = tree.getroot()

        for x in root.iter('name'):
            print(x.text)
            a = 'Button Buttonholes'
            # a = 'Crease Retention'
            # a = 'Dry Process'
            # a = 'Fabric Flaw'
            # a = "Fabric Hole"
            # a = 'Fabric Other'
            # a = 'Fabric Twisting'
            # a = 'Finishing Others'
            # a = 'Fin Stain Oil'
            # a = 'Fullness'
            # a = 'Hi Low'
            # a = 'Holes'
            # a = 'Loops'
            # a = 'Needle Damage'
            # a = 'Other Construction'
            # a = 'Out of Shade Range'
            # a = 'Pack Fold'
            # a = 'Pleat'
            # a = 'Pressing'
            # a = 'Print Embroidery'
            # a = 'Proc Splotch'
            # a = 'Puckering'
            # a = 'Raw Edge'
            # a = 'Rivets Bar tacks'
            # a = 'Run Off'
            # a = 'Seam Smoothness'
            # a = 'Sew Stain Oil'
            # a = 'Skipped Broken Stitch'
            # a = 'Threads Loose'
            # a = 'Threads Untrimmed'
            # a = 'Twisted Leg'
            x.text = str(a)

        os.chdir(path+'/'+folder)
        tree.write(file)
