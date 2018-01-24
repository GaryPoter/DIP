#! /usr/bin/env python
# -*- utf-8 -*-
# test1
# 1
# edu001
# 2018/1/21
# 20:52
import numpy as np
import cv2
img = cv2.imread('imgs/1.jpg')
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
for i in range(0, 8):
    cv2.imwrite('imgs2/%s.jpg' % i, img & (1 << i))
cv2.destroyAllWindows()