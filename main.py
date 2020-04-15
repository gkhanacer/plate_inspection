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
dirs = FileOperations.list_image_directories(validation_path)
print((len(validation_set) * len(tekrar) * len(once_sonra)) == len(dirs))

# IMAGE PROCESSING TEST
# im_path = validation_path + "/" + validation_set[4] + "/" + tekrar[2] + "/" + once_sonra[1] + "/" + "3.jpg"
# ImageProcessing.calculateDirtyInfo(im_path, show = False)