#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


# import sys
import os

# print(sys.path)   #
# print(sys.argv)   #打印相对路径


# res = os.popen("dir")

res = os.popen("dir").read()

print(res)



