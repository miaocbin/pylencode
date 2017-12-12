#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足如下条件，即是结果。
"""
#
# from math import sqrt
#
# i = 1
# while 1:
#     a, b = i + 100, i + 268
#     x, y = int(sqrt(a)), int(sqrt(b))
#     if x ** 2 == a and y ** 2 == i + 268:
#         print("%ld" % i)
#     i += 1

import math

for i in range(10000):
    # 转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i + 268):
        print(i)
