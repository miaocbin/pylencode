#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


# import getpass
#
# username = input("username:")
# password = getpass.getpass("password:")
#
# print(username,password)
#

_username = "alex li"
_password = 'abc123'

username = input("username:")
password = input("password:")
# password = getpass.getpass(password:)

if username == _username and password == _password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")








