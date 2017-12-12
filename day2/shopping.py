#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 

# 商品列表，每个商品用元组表示，商品可以增删改，商品属性不允许修改。
product_list = [
    ("Iphone",5299),
    ("Mac Pro",10800),
    ("Bicycle",800),
    ("Coffee",31),
    ("Python Book",102),
]
shopping_list = []

salary = input("Please input your salary: ")
if salary.isdigit:
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list,1):
            print(index,item)
        user_choice = input("Please what product you want to buy:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if len(product_list) > user_choice >= 0:
                shopping_list.append(user_choice)

    else:
        print("Invaild Input...")


print(product_list)


# print(type(int("-999")))
# print(int("-999"))





