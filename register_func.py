import os.path

from detectron2.structures import BoxMode
from detectron2.utils.logger import setup_logger
setup_logger()

def customDataloader():
    # with open(json_file) as f:
    #     data = json.load(f)
    files = os.listdir("register/test_detectron/")

    dataset_dicts = []
    # for i in range(len(labels)):
    i=0
    for file in files:
        # i=i+1
        record={}
        objs = []

        with open("register/test_detectron/"+file, "r") as f:
            lines = f.readlines()
            i=i+1
            record["file_name"]= "coco/train/"+file.replace("txt","jpg")#data["images"][i]["file_name"]
            record["width"]= 1920 #data["images"][i]["width"]
            record["height"]= 1080 #data["images"][i]["height"]
            record["image_id"]= i+1 #data["images"][i]["id"]
            for line in lines:
                obj = {
                    "bbox" : [int(line.split(' ')[1]), int(line.split(' ')[2]), int(line.split(' ')[3]), int(line.split(' ')[4])], #[data["annotations"][i]["bbox"][0],data["annotations"][i]["bbox"][1],data["annotations"][i]["bbox"][2],data["annotations"][i]["bbox"][3]],
                    "category_id" : 1,
                    "bbox_mode" : BoxMode.XYWH_ABS,
                }
                objs.append(obj)
                # i=i+1
            record["annotations"]= objs
        dataset_dicts.append(record)
        break
    return dataset_dicts

customDataloader()