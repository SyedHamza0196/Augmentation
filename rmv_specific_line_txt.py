import os

files = os.listdir("/home/macho/Desktop/Aletheia-AI/datasets/preprocess_and_validation/yolo_test/")
# print(files)
for file in files:
    with open("/home/macho/Desktop/Aletheia-AI/datasets/preprocess_and_validation/yolo_test/"+file, "r") as f:
        lines = f.readlines() #reads one line at a time
    with open("/home/macho/Desktop/Aletheia-AI/datasets/preprocess_and_validation/yolo_test/"+file, "w") as f:
        for line in lines:
            # if line[0] == "N":
            #     f.write(line)
            if line.split()[0] == "None":
                x = line.replace("None","0",1)
                f.write(x)