import albumentations as A
from albumentations.augmentations.functional import blur
import cv2
import os
import numpy as np

save_path = "/home/athar/Desktop/DataPilot/Projects/Levis/request"
folder = "/home/athar/Desktop/DataPilot/Projects/Levis/test_images"
images = os.listdir(folder)

for image in images:
    img = cv2.imread(folder+'/'+image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # transform = A.Blur(blur_limit=7, always_apply=True, p=1)
    transform = A.ColorJitter(
        brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2, always_apply=True, p=1)
    # transform = A.Emboss(alpha=(0.2, 0.5), strength=(
    #     0.2, 0.7), always_apply=True, p=1)
    # transform = A.GaussNoise(var_limit=(10.0, 50.0),
    #                          mean=0, per_channel=True, always_apply=True, p=1)
    # transform = A.ImageCompression(
    #     quality_lower=99, quality_upper=100, always_apply=True, p=1)
    # transform = A.MedianBlur(blur_limit=7, always_apply=True, p=1)
    # transform = A.MotionBlur(blur_limit=7, p=1)
    # transform = A.Sharpen(alpha=(0.2, 0.5), lightness=(
    #     0.5, 1.0), always_apply=True, p=1)
    # transform = A.Solarize(threshold=128, always_apply=True, p=1)
    # transform = A.RandomToneCurve(scale=0.1, always_apply=True, p=1)
    # transform = A.RandomGamma(gamma_limit=(
    #     80, 120), eps=None, always_apply=True, p=1)
    # transform = A.RandomBrightnessContrast(
    #     brightness_limit=0.2, contrast_limit=0.2, brightness_by_max=True, always_apply=True, p=1)
    # transform = A.RGBShift(r_shift_limit=20, g_shift_limit=20,
    #                        b_shift_limit=20, always_apply=True, p=1)
    # transform = A.InvertImg(p=1)

    transformed = transform(image=img)["image"]
    both = np.concatenate((img, transformed), axis=1)

    save_directory = 'colorJitter'
    os.chdir(save_path)
    if not os.path.exists(save_directory):
        os.mkdir(save_directory)
    os.chdir(save_directory)
    cv2.imwrite(image, both)
    # cv2.imshow('blur', both)
    # cv2.waitKey(0)
