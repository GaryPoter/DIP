#! /usr/bin/env python
# -*- utf-8 -*-
# test1
# sharpen_img
# edu001
# 2018/1/23
# 20:46
import cv2
import numpy as np
from imgLib import sharpen
import imgLib

if __name__ == '__main__':

    img = cv2.imread('imgs/1.jpg', cv2.CAP_MODE_GRAY)
    cv2.imshow('img', img)

    #  图片锐化
    img1 = sharpen(img, imgLib.x)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img + img1)

    #  图片模糊
    img2 = sharpen(img, imgLib.y)
    cv2.imshow('img3', img2)


    cv2.waitKey(0)
    cv2.destroyAllWindows()