#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


age_of_alex = 35
count = 0
guess_count = 3

while count < guess_count:
    guess_age = int(input("age:"))
    if guess_age == age_of_alex :
        print("You got it!")
        break
    elif guess_age > age_of_alex:
        print("guess smaller ...")
    else:
        print("guess bigger ...")
    count += 1
    if count == 3:
        confirm = input("Do you want to continue...?(y/n)")
        if confirm != "n":
            count = 0
# else:
#     print("You have tried too many times, fuck off!")

