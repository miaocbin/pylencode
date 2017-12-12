#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
#

# key-value
info = {
    "stu001": "ZhangSan Wu",
    "stu002": "Li Alex",
    "stu003": "Alex Shang",
}
'''
# 循环dict的正确姿势
for k in info:
    print(k,info[k])
'''
# 先把字典转换为列表，数据量大的时候不要使用
for k,v in info.items():
    print(k,v)


print(info.items())


