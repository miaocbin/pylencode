#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
# 


from pyzabbix import ZabbixAPI
import requests
import json

zapi = ZabbixAPI("http://mon.evun.cn")

zapi.login("miaochangbin","123456")


host = zapi.host.get(
    output = ['name','hostid'],

)