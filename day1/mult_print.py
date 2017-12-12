#!/usr/bin/env python3
# coding: utf-8
# __author__ = 'Administrator'
# for python3.x


# name = input('姓名：')
# age = input('年龄：')
# job = input('Job：')
# salary = input('请输入工资：')

# print("My name is ",name)

# info0 = '''
# --------- info of '''+ name +''' --------
# Name: ''' + name + '''
# Age: ''' + age + '''
# Job: ''' + age + '''
# Salary: ''' + salary + '''
# '''
#
# print(info0)
#

# info1 = '''
# --------- info of %s --------
# Name: %s
# Age: %s
# Job: %s
# Salary: %s
#
# ''' % (name,name,age,job,salary)
#
# print(info1)
#

name = input('姓名：')
age = int(input('年龄：'))    #integer
print (type(age),type(name))
job = input('Job：')
salary = int(input('请输入工资：'))

# info2 = '''
# ---------- info of %s ---------
# Name: %s
# Age: %d
# Job: %s
# Salary: %d
# ''' % (name,name,age,job,salary)
# print(info2)


# 格式化拼接，监控系统会用到，而且只能用这个。
# info3 = '''
# ---------- info of {Name} ---------
# Name: {Name}
# Age: {age}
# Job: {job}
# Salary: {salary}
# ''' .format(Name=name,age=age,job=job,salary=salary)
#
# print(info3)

info4 = '''
---------- info of {0} ---------
Name: {0}
Age: {1}
Job: {2}
Salary: {3}
''' .format(name,age,job,salary)

print(info4)

# 不到万不得已不要使用字符串拼接（,+)这种方式，上面的这种方式，只在内存中开辟一个内存块就完成
# +号拼接，会在内存中开辟好几块内存，效率地下，不要使用。

