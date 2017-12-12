#!/usr/bin/env python
# coding: utf-8
# __author__ = 'Administrator'
#
import json
from urllib import request, parse


ZABBIX_URL = 'http://mon.evun.cn'
ZABBIX_USERNAME = 'miaochangbin'
ZABBIX_PASSWORD = '123456'

url = "{}/api_jsonrpc.php".format(ZABBIX_URL)
header = {"Content-Type":"application/json"}

# auth user and password


# data = json.dumps {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": ZABBIX_USERNAME,
#         "password": ZABBIX_PASSWORD
#     },
#     "id" : = 1
# }

value = json.dumps(data).encode('utf-8')

req = request.Request(url, headers=header, data=value)

try:
    # 打开包装过的url
    result = request.urlopen(req)
except Exception as e:
    print("Auth Failed, Please Check Your Name And Password:", e)
else:
    response = result.read()
    # 上面获取的是bytes类型数据，故需要decode转化成字符串
    page = response.decode('utf-8')
    # 将此json字符串转化为python字典
    page = json.loads(page)
    result.close()
    print("Auth Successful. The Auth ID Is: {}".format(page.get('result')))





