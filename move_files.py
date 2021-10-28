import shutil
import os

source = "/home/athar/MEGA/augmented/randomBrightnessContrast"
source = "/home/athar/MEGA/original"
destination = "/home/athar/MEGA/images/train"

folders = os.listdir(source)
# print(folders)
for folder in folders:
    files = os.listdir(source+'/'+folder)
    # print(files)
    for file in files:
        shutil.move(source+'/'+folder+'/'+file, destination)
