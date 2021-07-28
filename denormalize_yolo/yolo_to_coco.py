from create_annotations import *
import numpy as np
import os

#################################################
# Change the classes depend on your own dataset.#
# Don't change the list name 'Classes'          #
#################################################

def get_files():
    files = os.listdir("train/")
    for file in files:
        with open("train/"+file, "r") as f:
            lines = f.readlines() #reads one line at a time
            # print(lines[0].split(' ')[1])
        with open("test_detectron/"+file, "w") as f:
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
                
                f.write("0 "+min_x+" "+min_y+" "+width+" "+height+"\n")

get_files()
# Class에 맞게 바꿔줘야함
# classes = [
# "bag",
# ]

# # Get 'images' and 'annotations' info
# def images_annotations_info(opt):

#     path = opt.path
#     # path : train.txt or test.txt
#     annotations = []
#     images = []

#     file = open(path, "r")
#     read_lines = file.readlines()
#     file.close()

#     image_id = 0
#     annotation_id = 1   # In COCO dataset format, you must start annotation id with '1'

#     for line in read_lines:
#         # Check how many items have progressed
#         if image_id % 1000 == 0:
#             print("Processing " + str(image_id) + " ...")

#         line = line.replace('\n', '')
#         img_file = cv2.imread(line)

#         # read a label file
#         label_path = line[:-3]+"txt"
#         label_file = open(label_path,"r")
#         label_read_line = label_file.readlines()
#         label_file.close()

#         h, w, _ = img_file.shape

#         # Create image annotation
#         image = create_image_annotation(line, w, h, image_id)
#         images.append(image)

#         # yolo format - (class_id, x_center, y_center, width, height)
#         # coco format - (annotation_id, x_upper_left, y_upper_left, width, height)
#         for line1 in label_read_line:
#             label_line = line1
#             category_id = int(label_line.split()[0]) + 1    # you start with annotation id with '1'
#             x_center = float(label_line.split()[1])
#             y_center = float(label_line.split()[2])
#             width = float(label_line.split()[3])
#             height = float(label_line.split()[4])

#             int_x_center = int(img_file.shape[1]*x_center)
#             int_y_center = int(img_file.shape[0]*y_center)
#             int_width = int(img_file.shape[1]*width)
#             int_height = int(img_file.shape[0]*height)

#             min_x = int_x_center-int_width/2
#             min_y = int_y_center-int_height/2
#             width = int_width
#             height = int_height

#             annotation = create_annotation_yolo_format(min_x, min_y, width, height, image_id, category_id, annotation_id)
#             annotations.append(annotation)
#             annotation_id += 1

#         image_id += 1  # if you finished annotation work, updates the image id.

#     return images, annotations

# def get_args():
#     parser = argparse.ArgumentParser('Yolo format annotations to COCO dataset format')
#     parser.add_argument('-p', '--path', type=str, help='Absolute path for \'train.txt\' or \'test.txt\'')
#     parser.add_argument('--debug', action='store_true' ,help='Visualize bounding box and print annotation information')
#     parser.add_argument('--output', type=str, help='Name the output json file')

#     args = parser.parse_args()
#     return args

# if __name__ == '__main__':
#     opt = get_args()
#     output_name = opt.output
#     # output_path = 'output/' + output_name + '.json'

#     print("Start!")

#     # start converting format
#     coco_format['images'], coco_format['annotations'] = images_annotations_info(opt)

#     for index, label in enumerate(classes):
#         ann = {
#             "supercategory": "Disinfect_5obj",
#             "id": index + 1,  # Index starts with '1' .
#             "name": label
#         }
#         coco_format['categories'].append(ann)

#     with open(output_path, 'w') as outfile:
#         json.dump(coco_format, outfile)

#     print("Finished!")
