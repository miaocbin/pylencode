#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
#

"""
字典的特性：
    dict是无序的
    key必须是唯一的,so 天生去重
"""

# key-value
info = {
    "stu001": "ZhangSan Wu",
    "stu002": "Li Alex",
    "stu003": "Alex Shang",
}

print(info)
# 改，给已存在的key一个新值就是修改
info["stu001"] = "Wu TengLan"
print(info)

# 增 ,赋予新key一个value，就是增加了
info["stu004"] = "Zhang ZiYang"
print(info)

# 查
# info["stu001"]
print(info.get("stu001"))
print(info.get("stu009"))

# 判断key是否存在
print("stu003" in info)
# python2： info.has_key("stu003")

# 删除用pop，蹦出来,删除字典的标准姿势
print(info.pop("stu003"))

# 也可以这样删除字典中的元素
del info["stu002"]
print(info)
# 随机删除字典中的元素
info.popitem()
print(info)




