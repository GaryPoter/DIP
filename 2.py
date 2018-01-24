#! /usr/bin/env python
# -*- utf-8 -*-
# test1
# 2
# edu001
# 2018/1/21
# 20:58
import cv2
img = cv2.imread('imgs2/4.jpg')
for i in range(5, 8):
    img = img + cv2.imread('imgs2/%s.jpg' % i)
    cv2.imshow('img%s' % i, img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyWindow('img')