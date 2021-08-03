import os

def get_files():
    if not os.path.exists('result_new'):
        os.mkdir('result_new')
    files = os.listdir("1cls_personBag_3243_concise/labels/train/")
    iter=1
    for file in files:
        with open("1cls_personBag_3243_concise/labels/train/"+file, "r") as f:
            lines = f.readlines() #reads one line at a time
            # print(lines[0].split(' ')[1])
        with open("result_new/"+file, "w") as f:
            for line in lines:
                xc = float(line.split(' ')[1])
                yc = float(line.split(' ')[2])
                width = float(line.split(' ')[3])
                height = float(line.split(' ')[4])

                int_x_center = int(1920*xc)
                int_y_center = int(1080*yc)
                int_width = int(1920*width)
                int_height = int(1080*height)

                min_x = str(int(int_x_center-int_width/2))
                min_y = str(int(int_y_center-int_height/2))
                width = str(int(int_width))
                height = str(int(int_height))
                
                f.write(str(0)+" "+min_x+" "+min_y+" "+width+" "+height+"\n")
            iter=iter+1

get_files()
