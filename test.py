#流程测试脚本
import time

from memberinfo import member
from cf import *
from showping import showping
from  order import order
from login import Login
from business import Business
from Common.common import Common
import json
membertoken=shopkeeper_token
businesstoken=supplier_token
admin_token=operation_token
# token=Login().login()
#Bearer
#token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaG90Zml4LnNodWl4aW9uZ2tlamkubmV0XC9hcHBcL0xvZ2luQnlINSIsImlhdCI6MTU1OTIxNzM5NSwiZXhwIjoxNTU5MjE3OTk1LCJuYmYiOjE1NTkyMTczOTUsImp0aSI6ImtZYTQ0bWdYTk45bHJEYnAiLCJzdWIiOjQwOTA3LCJwcnYiOiI2ZDliZGYzYTkwNTc2YTdhNjJmOGNjNWQyYzViYjZmOGVhY2FkODE3IiwiaWQiOjQwOTA3LCJyb2xlIjoiVVNFUiIsImlzX3VzZXIiOnRydWUsInJvbGVfaWQiOjAsInJlc2V0X3RpbWUiOiIyMDE5LTA1LTA1IDE2OjE3OjEyIiwib3BlbmlkIjoib0hGWEkxQXgydVBLWWFYWXVqSjZpQlR4elVScyIsInRoaXJkX3BhcnRfaWQiOjEzNTkyNH0.cDc6CXnfCXQ9MOf2hdQbDEA4wI6HjIZ0geNff5BULnA'
#businesstoken='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaG90Zml4LnNodWl4aW9uZ2tlamkubmV0XC9CdXNpbmVzc0F1dGhzIiwiaWF0IjoxNTU5MzA5MDE4LCJleHAiOjE1NjA1MTg2MTgsIm5iZiI6MTU1OTMwOTAxOCwianRpIjoiZmNEaUNkR2JoMEdESlJWYyIsInN1YiI6MzUsInBydiI6IjQ4NTA2NTc3M2QxNTAzNGQ0MjU1YWY2MzQwMzFhNGQyYzQyYTU1NGUiLCJpZCI6MzUsInJvbGUiOiJCVVNJTkVTUyIsImFjY291bnRfaWQiOjM1LCJyZXNldF90aW1lIjpudWxsLCJyb2xlX2lkIjozNSwiaXNfYnVzaW5lc3MiOnRydWUsImJ1c2luZXNzX2lkIjozNX0.oQDaZkrjEo-GmAecinSlfWdk8Vr8QUQ5SECy_IM28fM'
memberinfo=member()
# memberinfo.userinfo(membertoken)  #用户信息

# show=showping()
# indexshow=show.indexshowping(membertoken)
# shownoe=show.showpinginfo(indexshow[0],membertoken)


order=order()
bulidorder=order.bulidorder(membertoken,1,0) #创建订单
trade_no=bulidorder[0]
short_no=bulidorder[1]
nun=bulidorder[2]
money=bulidorder[3]
pyorder=order.payorder(membertoken,trade_no) #余额购买

# qxzhifuorder=order.qxzhifuorder(membertoken,short_no) # 取消已支付订单
# s=order.nopayquxiao(membertoken,trade_no)

order_data=order.myorder(membertoken)# 我的订单
# price=order_data[2]
sub_order_id=order_data[0]
order_id=order_data[1]
businessadmin=Business()
take=businessadmin.takeshoping(businesstoken,order_id)#拣货
fahuo=businessadmin.fahuo(businesstoken,membertoken,short_no,sub_order_id,nun)#发货
# sub_order_id=2677894
memberinfo.SingleOrders(admin_token,sub_order_id)#签收
# time.sleep(60)
# sub_order_id=2699490
# price='180'
# SaleOrder_id,price=memberinfo.CreateSaleOrder(sub_order_id,int(money),3,1) #创建售后单
# memberinfo.SupplySaleOrder(SaleOrder_id)#用户补充
# memberinfo.SaleOrderHandle(int(SaleOrder_id),3)#审核
# memberinfo.SaleOrderClose(int(SaleOrder_id),price)#结案


#buildshoping=businessadmin.post_products_keyattr(businesstoken)

