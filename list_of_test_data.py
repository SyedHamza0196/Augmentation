import os, random
from pathlib import Path
from shutil import copyfile

def load_images_from_folder(folder):
    labels = []
    for x in os.listdir(folder):
        filename, file_extension = os.path.splitext(x)
        new_filename = "/app/home/server1/hamza/v5/Pedestrian/dataset/images/train/"+filename+".jpg\n"
        labels.append(new_filename)

    file1 = open("val_data.txt","w")
    file1.writelines(labels)
    file1.close()

folder='/home/macho/Desktop/Aletheia-AI/datasets/fasial_person/images/train/'
load_images_from_folder(folder)