#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
# import imutils
from algorithms import ImageProcessing

import os

class FileOperations:
    
    @staticmethod
    def list_files(startpath, ftype=".jpg", debug=True):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(startpath):
            for file in f:
                if ftype in file:
                    files.append(os.path.join(r, file))

        if debug:
            for f in files:
                print(f)

        return files

    @staticmethod
    def list_image_directories(startpath, debug=True):
        files = FileOperations.list_files(startpath, debug=debug)
        directories = set()
        for f in files:
            dir = f[:-5]
            directories.add(dir)

        if debug:
            for d in directories:
                print(d)
            print(len(directories))
        return list(directories)

    @staticmethod
    def getDirectoryList(in_this_path):
        return filter(lambda x: os.path.isdir(in_this_path + "/" + x), os.listdir(in_this_path))