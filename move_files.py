import shutil
import os

source = "/home/athar/MEGA/taggedData/FabricTwisting/"
destination = "/home/athar/MEGA/augmented/test/colorJitter/FabricTwisting/"

files = os.listdir(source)

for file in files:
    if file.split('.')[-1] == 'xml':
        shutil.move(source+'/'+file, destination)
