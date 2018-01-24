#! /usr/bin/env python
# -*- utf-8 -*-
# test1
# imgLib
# edu001
# 2018/1/24
# 13:15
import numpy as np

#  拉普拉斯算子
x = -1 * np.array([[0, 1, 0],
              [1, -4, 1],
              [0, 1, 0]], dtype='uint8')

#  模糊算子
y = 1/16 * np.array([[1, 2, 1],
              [2, 4, 2],
              [1, 2, 1]], dtype='uint8')




def sharpen(img, f=None):
    rows = img.shape[0]
    cols = img.shape[1]

    #  填充
    template = np.zeros((rows + 2, cols + 2), dtype='uint8')
    result = np.zeros((rows + 2, cols + 2), dtype='uint8')
    template[1: -1, 1: -1] = img

    #  处理
    for i in range(1, rows + 1):
        for j in range(1 , cols + 1):
            tmp = template[i-1: i+2, j-1: j+2]
            p = np.sum(tmp * f)
            result[i, j] = p

    # img = template[1: -1, 1: -1]
    return result[1: -1, 1: -1]
