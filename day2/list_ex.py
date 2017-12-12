#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


# list
'''
names = ["Alex","TengLan","Eric","Jack","Rain","Tome","Amy"]

print(names[3])
# 列表切片，顾头不顾尾
print(names[1:4])
# 取下表1到-1的值，不包括-1
print(names[1:-1])
# 首尾下表均可省，如果需要取到最后一个，必须这么写
print(names[1:])
print(names[:])

print(names[:4])
# 只取列表的最后一个元素
print(names[-1:])

# 每隔一个元素取一个
print(names[::2])
# 或者,效果一样
print(names[0::2])

# 在列表后面追加一个元素
names.append("我是新来的")
print(names)

# 在列表中间指定位置插入一个元素
names.insert(2,"强行在Eric前面插入")
print(names)

names.insert(4,"从Eric后面试试新姿势")
print(names)

# 修改列表元素的值
names[2]="该换人了"
print(names)

# 删除列表元素
del names[2]
print(names)
# 删除指定元素
names.remove("Eric")
print(names)
# 删除最后一个元素
names.pop()
print(names)
'''


# 列表扩展
a = [1,9,3]
b = [4,8,9,3,6]

a.extend(b)
print(a)
print(b)

a_copy = a.copy()
print(a_copy)

# 统计某个元素的个数
c = a_copy.count(1)
print(c)

# 列表排序
print(a_copy)
print(a_copy.sort())
# 列表反转
a_copy.reverse()
print(a_copy)

# 获取下标,只返回找到的第一个下标
print(a_copy.index(9))

print(a_copy.count(9))

