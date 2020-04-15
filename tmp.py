#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
# import imutils


def getAreaOfImage(im):
    th = 128
    im_bool = im > th
    return np.sum(im_bool)

base_path = "/media/sf_shared/image_processing"
validation_path = base_path + "/validation"
valid_1 = validation_path + "/S1_0.2Hz_15mm_7dk"
tekrar = valid_1 + "/tekrar_1"

img_rgb = cv2.imread(tekrar + "/o/1.jpg", 1)
img = cv2.imread(tekrar + "/o/1.jpg", cv2.IMREAD_GRAYSCALE)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

# Copy the thresholded image.
im_floodfill = thresh1.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = thresh1.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
mask2 = np.zeros((h, w), np.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, None, (0,0), 255)

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.
im_out = cv2.bitwise_or(thresh1, im_floodfill_inv) # thresh1 | im_floodfill_inv
plate_area = getAreaOfImage(im_out)

# Find largest contour
_, contours, hierarchy = cv2.findContours(im_out, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
if len(contours) != 0:
    c = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)
    # draw the biggest contour (c) in green 
    cv2.rectangle(img_rgb, (x,y), (x+w,y+h), (0,255,0), 2)

    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    cv2.circle(img_rgb, center,100,(255,0,0),-1)
    radius = int(radius)
    cv2.circle(img_rgb, center,radius,(0,0,255), 11)

    small_plate = mask2.copy()
    small_plate_rad = radius - (float(radius * 2) / (float(19) /  2))
    cv2.circle(small_plate, center, int(small_plate_rad), (255,255,255), -1)

    dirty = cv2.bitwise_and(small_plate, im_floodfill_inv)

    dirty_area = getAreaOfImage(dirty)

    rate = float(dirty_area)/plate_area
    print("Plate area: {}\tDirty area: {}\tRate of dirty/plate: {}".format(plate_area, dirty_area, rate))


def get_dirty():
    return dirty

# Display images.
# cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.namedWindow('img_rgb', cv2.WINDOW_NORMAL)
cv2.namedWindow('thresh1', cv2.WINDOW_NORMAL)
cv2.namedWindow('im_floodfill', cv2.WINDOW_NORMAL)
cv2.namedWindow('im_floodfill_inv', cv2.WINDOW_NORMAL)
cv2.namedWindow('Foreground', cv2.WINDOW_NORMAL)
cv2.namedWindow('small_plate', cv2.WINDOW_NORMAL)
cv2.namedWindow('dirty', cv2.WINDOW_NORMAL)
# cv2.imshow("mask", mask)
cv2.imshow("img_rgb", img_rgb)
cv2.imshow("thresh1", thresh1)
cv2.imshow("im_floodfill", im_floodfill)
cv2.imshow("im_floodfill_inv", im_floodfill_inv)
cv2.imshow("Foreground", im_out)
cv2.imshow("small_plate", small_plate)
cv2.imshow("dirty", dirty)
cv2.waitKey(0)

# titles = ['Original Image','BINARY','BINARY_INV', 'mask', 'im_floodfill','im_floodfill_inv','im_out']
# images = [img, thresh1, thresh2, mask, im_floodfill, im_floodfill_inv, im_out]

# len_image = len(images)
# for i in xrange(len_image):
#     plt.subplot(2, 4, i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# k = cv2.waitKey(0)

# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()
