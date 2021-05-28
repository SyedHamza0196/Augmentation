import os

bag=belt=1
what = 1

files = os.listdir("/home/hamza/MEGA/pioneer/4664/labels/train/")
# print(files)
for file in files:
    with open("/home/hamza/MEGA/pioneer/4664/labels/train/"+file, "r") as f:
        lines = f.readlines() #reads one line at a time
    # with open("/home/macho/Desktop/Aletheia-AI/datasets/preprocess_and_validation/yolo_test/"+file, "w") as f:
        for line in lines:
            if line.split()[0] != "0":
                what+=1
                print(file)
            if line.split()[0] != "1":
                what+=1
                print(file)
print(":( :",what) #,"\n",'belt:',belt)