#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

class ImageProcessing:

    PLATE_DIAMETER = 19 # cm
    GAP = 2 # cm

    @staticmethod
    def defineWindows():
        # cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
        cv2.namedWindow('img_rgb', cv2.WINDOW_NORMAL)
        cv2.namedWindow('thresh', cv2.WINDOW_NORMAL)
        cv2.namedWindow('im_floodfill', cv2.WINDOW_NORMAL)
        cv2.namedWindow('im_floodfill_inv', cv2.WINDOW_NORMAL)
        cv2.namedWindow('plate', cv2.WINDOW_NORMAL)
        cv2.namedWindow('small_plate', cv2.WINDOW_NORMAL)
        cv2.namedWindow('dirty', cv2.WINDOW_NORMAL)

    @staticmethod
    def readImage(im_path):
        # Read image as rgb and convert to grayscale
        img_rgb = cv2.imread(im_path, 1)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        return img_rgb, img_gray

    @staticmethod
    def createBlackMask(bin_image):
        h, w = bin_image.shape[:2]
        mask = np.zeros((h, w), np.uint8)
        return mask

    @staticmethod
    def getAreaOfImage(im):
        th = 128
        im_bool = im > th
        return np.sum(im_bool)

    @staticmethod
    def getLargestContour(bin_image):
        # Find largest contour
        _, contours, hierarchy = cv2.findContours(bin_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) != 0:
            c = max(contours, key = cv2.contourArea)
            return c
        return None

    @staticmethod
    def determineOnlyDirtPart(im_plate, im_floodfill_inv, center, radius):
        small_plate = ImageProcessing.createBlackMask(im_plate)
        plate_radius = (float(ImageProcessing.PLATE_DIAMETER) /  2)
        small_plate_rad = radius - (float(radius * ImageProcessing.GAP) / plate_radius)
        cv2.circle(small_plate, center, int(small_plate_rad), (255,255,255), -1)
        dirty_part = cv2.bitwise_and(small_plate, im_floodfill_inv)
        return small_plate, dirty_part

    @staticmethod
    def showOpenCvImages(titles, images):

        # for i in range(0, len(titles)):
        #     cv2.namedWindow(titles[i], cv2.WINDOW_NORMAL)
        #     cv2.imshow(titles[i], images[i])
        cv2.namedWindow(titles[1], cv2.WINDOW_NORMAL)
        cv2.imshow(titles[1], images[1])
        cv2.namedWindow(titles[0], cv2.WINDOW_NORMAL)
        cv2.imshow(titles[0], images[0])
        cv2.waitKey(0)

    @staticmethod
    def showMatplotlipImages(titles, images, im_path, show=False, save_plot=False):
        len_image = len(images)
        for i in xrange(len_image):
            plt.subplot(2, 4, i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])

        if show:
            plt.show()

        if save_plot:
            im_path = im_path.replace("/", "_")
            im_path = "/media/sf_shared/image_processing/gorsel/result/"+im_path[45:]
            plt.savefig(im_path, dpi=720)
            print("Figure saved: {}: ".format(im_path))
            plt.clf()

    @staticmethod
    def calculateDirtyInfo(im_path, debug = True, show = False, save_plot=False):
        # Read image as rgb and  grayscale
        img_rgb, img_gray = ImageProcessing.readImage(im_path)

        # Convert grayscale to binary for appearing plate
        ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

        # Copy the thresholded image.
        im_floodfill = thresh.copy()

        # Floodfill from point (0, 0) to obtain only black dirty on white scene
        cv2.floodFill(im_floodfill, None, (0,0), 255)

        # Invert floodfilled image to obtain only white dirty on black scene
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)

        # Combine the two images to get the foreground/plate.
        im_plate = cv2.bitwise_or(thresh, im_floodfill_inv) # thresh | im_floodfill_inv
        plate_area = ImageProcessing.getAreaOfImage(im_plate)

        # Get largest contour to obtain only plate connected component
        c = ImageProcessing.getLargestContour(im_plate)
        if c is not None:
            # Fit a circle on plate
            (x,y),radius = cv2.minEnclosingCircle(c)

            # Determine center and radius of circle
            center = (int(x),int(y))
            radius = int(radius)
            if show:
                # Show center
                cv2.circle(img_rgb, center, 100,(255,0,0),-1)
                # Show fitted cirle on plate
                cv2.circle(img_rgb, center,radius,(0,0,255), 11)

            small_plate, dirty_part = ImageProcessing.determineOnlyDirtPart(im_plate, im_floodfill_inv, center, radius)

            dirty_area = ImageProcessing.getAreaOfImage(dirty_part)

            dirt_plate_rate = float(dirty_area)/plate_area
            print("Plate area: {}\tDirty area: {}\tRate of dirty/plate: {}".format(plate_area, dirty_area, dirt_plate_rate))
            
            if show or save_plot:
                titles = ['img_rgb','thresh','im_floodfill', 'im_floodfill_inv', 'im_plate','small_plate','dirty']
                images = [img_rgb, thresh, im_floodfill, im_floodfill_inv, im_plate, small_plate, dirty_part]
                # ImageProcessing.showOpenCvImages(titles, images)
                ImageProcessing.showMatplotlipImages(titles, images, im_path, show=show, save_plot=save_plot)

            return plate_area, dirty_area, dirt_plate_rate
        
        else:
            print("There is no plate in that image: {}".format(im_path))


