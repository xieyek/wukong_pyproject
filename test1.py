#coding=utf-8
import json
import time
import psutil
import pymysql
import socket
import pexpect
from sql import *
import paramiko
import random
import requests
from Common.common import Common
import cf
from memberinfo import member
from order import *
#获取计算机名称
# hostname=socket.gethostname()
# #获取本机IP
# ip=socket.gethostbyname(hostname)
# print(ip)



# def SaleOrderRefund():
#     url = 'http://h5.shuixiongkeji.net/app/GenerateDailySaleOrder'
#     header = {'Content-Type': 'application/json',
#               'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaDUuc2h1aXhpb25na2VqaS5uZXRcL2FwcFwvTG9naW5CeUg1IiwiaWF0IjoxNTYxMDEzNzIwLCJleHAiOjE1NjEwMjA5MjAsIm5iZiI6MTU2MTAxMzcyMCwianRpIjoiVXdjajRUSGFja1JYb2h5eCIsInN1YiI6NDgyOTgsInBydiI6IjZkOWJkZjNhOTA1NzZhN2E2MmY4Y2M1ZDJjNWJiNmY4ZWFjYWQ4MTciLCJpZCI6NDgyOTgsInJvbGUiOiJVU0VSIiwiaXNfdXNlciI6dHJ1ZSwicm9sZV9pZCI6MCwicmVzZXRfdGltZSI6IjIwMTktMDYtMDkgMTk6MDY6NDIiLCJvcGVuaWQiOiJvVmtBbzU1UUtQNWJEcklud25oOEZWQTBXcHNRIiwidGhpcmRfcGFydF9pZCI6MzMyNDA5fQ.wAwaVvv4xQXBVevUUpkmXQP0H2Df8GlKPc74YqiSdfI'
#               }
#     date ={"is_platform":"1",
#            "area_code":110101,
#            "product_sku_id":12175,
#            "product_num":1,
#            "daily_sale_id":263,
#            "buy_type":"",
#            "product_attr_val_id":0,
#            "contacter":"你们",
#            "province":"北京市",
#            "city":"北京市",
#            "area":"东城区",
#            "address":"哈喽",
#            "mobile":"13613047537",
#            "remark":"",
#            "selected_order_label_array":[],
#            "freight":"",
#            "is_gift":0,
#            "gift_text":"",
#            "freight_template_id":814}
#     data1 = Common.dumps_text(date)
#     req = requests.post(url=url, headers=header,data=data1)
#     print(req.json())

a=Common.random_num(4)
print('明天打咪奖？')
print('还用说，当然是：'+a)



