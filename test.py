#! /usr/bin/env python
# -*- utf-8 -*-
# test1
# test
# edu001
# 2018/1/24
# 13:10
import numpy as np

x = np.array([[0, 1, 0],
              [1, -4, 1],
              [0, 1, 0]])
print(x * x)
print(np.sum(x * x))