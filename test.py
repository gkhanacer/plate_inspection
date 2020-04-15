#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
# import imutils
from algorithms import ImageProcessing

import os
from files import FileOperations

base_path = "/media/sf_shared/image_processing"
validation_path = base_path + "/validation"
validation_set = ["S1_0.2Hz_15mm_7dk", "S1_0.2Hz_25mm_15dk", 
                "S1_1Hz_15mm_15dk", "S1_1Hz_25mm_7dk", 
                "S7_0.2Hz_15mm_15dk", "S7_0.2Hz_25mm_7dk", 
                "S7_1Hz_15mm_7dk", "S7_1Hz_25mm_15dk"]
tekrar = ["t_1", "t_2", "t_3"]
once_sonra = ["o", "s"]

# FILE TEST
# dirs = FileOperations.list_image_directories(validation_path)
# print((len(validation_set) * len(tekrar) * len(once_sonra)) == len(dirs))

# IMAGE PROCESSING TEST
# im_path = validation_path + "/" + validation_set[4] + "/" + tekrar[2] + "/" + once_sonra[1] + "/" + "2.jpg"
im_path = "/media/sf_shared/image_processing/test/S7_0.5Hz_25mm_60/t_2/s/IMG_20200319_17165"
ImageProcessing.calculateDirtyInfo(im_path, show = True, save_plot=False)

# IMAGE PROCESSING VISUAL TEST
test_images = ["/media/sf_shared/image_processing/validation/S1_0.2Hz_15mm_7dk/t_2/o/2.jpg", 
"/media/sf_shared/image_processing/validation/S1_0.2Hz_25mm_15dk/t_3/s/1.jpg", 
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_1/s/1.jpg",  
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_3/o/3.jpg", 
"/media/sf_shared/image_processing/validation/S1_1Hz_25mm_7dk/t_2/o/4.jpg",  
"/media/sf_shared/image_processing/validation/S7_0.2Hz_15mm_15dk/t_3/o/3.jpg", 
"/media/sf_shared/image_processing/validation/S7_0.2Hz_25mm_7dk/t_3/s/2.jpg", 
"/media/sf_shared/image_processing/validation/S7_1Hz_15mm_7dk/t_1/s/3.jpg", 
"/media/sf_shared/image_processing/validation/S7_1Hz_25mm_15dk/t_1/s/1.jpg", 
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/s/6.jpg",  
"/media/sf_shared/image_processing/validation/S7_0.2Hz_15mm_15dk/t_2/s/1.jpg", 
"/media/sf_shared/image_processing/validation/S7_1Hz_15mm_7dk/t_2/o/5.jpg", 
"/media/sf_shared/image_processing/validation/S7_0.2Hz_15mm_15dk/t_3/o/1.jpg", 
"/media/sf_shared/image_processing/validation/S1_1Hz_25mm_7dk/t_3/o/2.jpg", 
"/media/sf_shared/image_processing/validation/S1_0.2Hz_25mm_15dk/t_2/o/3.jpg"]

# ImageProcessing.calculateDirtyInfo(test_images[15], show = False, save_plot=True)

# k = 7
# for i in range(k,k+3):
#     print(i)
#     ImageProcessing.calculateDirtyInfo(test_images[i], show = False, save_plot=True)

# NEW TEST

test_images = ["/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_1/o/1.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_1/o/2.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_1/o/3.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/o/1.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/o/2.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/o/3.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_3/o/1.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_3/o/2.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_3/o/3.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_1/s/1.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_1/s/2.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_1/s/3.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/s/1.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/s/2.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/s/3.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_2/s/1.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_3/s/2.jpg",
"/media/sf_shared/image_processing/validation/S1_1Hz_15mm_15dk/t_3/s/3.jpg"]

# # k = 7
# for i in range(0,18):
#     print(i)
#     ImageProcessing.calculateDirtyInfo(test_images[i], show = False, save_plot=True)