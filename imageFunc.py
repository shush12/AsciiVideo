import cv2
import numpy as np


ASCII_PIXELS = ("N@#W$9876543210?!abc;:+=_,-.                                ")[::-1]
scale = len(ASCII_PIXELS) - 1

def GetImageAverages(img):
    # Needed character from ASCII_PIXELS will be chosen by evaluating the
    # Pixel's brightness - averaging RGB.
    # The higher the number the Brighter the pixel.

    new_img = np.zeros(img.shape[:2], dtype=np.int8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            avg = np.abs(np.sum(img[i, j]) / 3)
            new_img[i, j] = avg

    # print(sorted(list(new_img.flatten())))
    # cv2.imshow("", new_img / 255.)
    # cv2.waitKey()
    return new_img / 255 * scale

