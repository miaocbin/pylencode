#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


"""
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。
"""


a = (1, 2, 3, 4)
for b1 in a:
    for b2 in a:
        for b3 in a:
            if b1 != b2 and b2 != b3 and b1 != b3:
                print("%d%d%d" % (b1, b2, b3))

