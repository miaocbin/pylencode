#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天。
"""

"""
import datetime
t=datetime.date(input("Year:"),input("Month:"),input("Day:"))
n=datetime.date(datetime.date.today().year,1,1)
print((t-n).days+1)
"""

year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 <= month <= 12:
    sum1 = months[month - 1]
else:
    print('data error')
sum1 += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum1 += 1
print('it is the %dth day.' % sum1)
