from login import Login
import requests
import json
from datetime import *
from http_method import Http
from Common.common import Common
from sql import Mysql
from cf import *
import math
H5_url='http://h5.shuixiongkeji.net/'
admin_token=operation_token
common=Common()
class member():
 def userinfo(self,token):
        url=Common.first_url()+'app/MrdMemberInfo'
        #url = "https://hotfix.shuixiongkeji.net/app/MrdMemberInfo"
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token
            # "cookie": "token="+ membertoken
        }
       # res = requests.request("GET",url, headers=headers)
        res = requests.get(url=url,headers=headers)
        resdata=res.json()['data']
       # res=Http.get(url,None,token)
        if (res.status_code==200):
            print('用户信息获取成功：'+ str(resdata) )
            return resdata['id'],resdata['balance'],resdata['agent_level'],resdata['stock'],resdata['rec_member_id'],resdata['member_card_profit'],resdata['current_level_name']

        else:
            print('用户信息获取失败：' + str(res))

 # def memberuplv(self):
 #     c =10000000
 #     a=[[0,100,1],[101,300,2],[301,1000,3],[1001,2500,4],[2501,5000,5],[5001,15000,6],[15001,25000,7],[25001,40000,8],
 #        [40001,60000,9],[60001,100000,10],[100001,150000,11],[150001,170000,12],[170001,250000,13],[250001,350000,14],
 #        [350001,500000,15],[500001,700000,16],[700001,1000000,17],[1000001,2000000,18],[2000001,5000000,19],[5000001,8880000,20]]
 #     if(c<=8880000):
 #      for b in a:
 #        if ( c >= b[0]<= b[1]):
 #            if(c<=b[1]):
 #                  print(b[2])
 #     else:
 #                print(20)
 def CreateSaleOrder(self,sub_order_id,money,sale_type,num): #创建售后单
     sql='SELECT id FROM daily_sale_orders WHERE order_id=%d;'%sub_order_id
     obj=Mysql().sqlclien(sql)[0][0]
     token1 =admin_token
     url=Common.first_url()+ 'admin/CreateSaleOrder'
     url1='http://10.0.0.137'
     headers = {
         'Content-Type': "application/json",
         'Authorization':token1
       #"cookie": "token="+ membertoken
     }
     data={
         "order_id":obj,    #dali_order的id
        # 'job_order_id': [6],
         'sale_problem_id': 11,
         'sale_type':sale_type,
         'problem_remark': '5132',
         'number': num,
         'operator_action':'客服备注',

         'pay_data':[
                      {'pay_data_id': 1, 'money': str(money * num) },
                          {'pay_data_id': 2, 'money': '0.01'},
              {'pay_data_id': 3, 'money': '0.01'}
                     ]
     }
     r=requests.post(url,data=common.dumps_text(data),headers=headers)
     if r.status_code==200:
         print('创建售后订单信息：' + str(r.json()))
     else:raise NameError(r.status_code)
     return r.json()['data']['id'],str(money * num)
 def ConsultativeHistory(self): #协商历史
     membertoken=shopkeeper_token
     url =Common.first_url()+ 'app/ConsultativeHistory'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': membertoken
         # "cookie": "token="+ membertoken
     }
     data = {
         'order_id': 2666009,
        # 'consumer_id':1140748,

     }
     r = requests.get(url, data=data, headers=headers)
     print(r.json())
 def SaleOrderHandle(self,id,status):#售后单(审核|取消|关闭
      token1 = admin_token
      url =Common.first_url()+'admin/SaleOrderHandle'
      headers = {
          # Bearer
          'Content-Type': "application/json",
          'Authorization': token1
          # "cookie": "token="+ membertoken
      }
      data = {
          'id':id,
          'status':status,
          'remark':'dwdwdcwfwfw',
          'describe':'87488489'
      }
      r = requests.post(url, data=json.dumps(data), headers=headers)
      print('审核信息：'+'售后id:'+str(id)+' '+str(r.json()))
 def SaleOrderClose(self,id,money): #售后单结案
     token1 = admin_token
     url =Common.first_url()+'admin/SaleOrderClose'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }
     date = {
         "id": id,
         'pay_type': 1,
         'delivery_id':24,
         'delivery_no':'484646546454',
         # 'account':'18000000417',
         # 'account_name':'哈哈哈',
         # 'job_order_no':'24888150',
         'pay_data': [
             {'pay_data_id': 1,  'money': money},
              {'pay_data_id': 2,'money': '0.01'},
                      {'pay_data_id': 3,  'money': '0.01'}
        ]
     }
     r = requests.post(url, data=json.dumps(date), headers=headers)
     print('结案信息：'+ str(r.json()))
 def PostSaleOrders(self):#售后工单列表供应商
     token2=supplier_token
     url = Common.first_url()+'seller/PostSaleOrders'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token2
         # "cookie": "token="+ membertoken
     }
     r = requests.get(url, headers=headers)
     print(r.json())
 def admin_PostSaleOrders(self):#售后工单列表总后台

     token1 = admin_token
     url = Common.first_url(2)+ 'admin/PostSaleOrders'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }

     r = requests.get(url,None,headers=headers)
     print(r.json())
 def SaleOrderRefund(self): #售后退款记录
     token1 = admin_token
     url =Common.first_url()+'admin/SaleOrderRefund'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }
     date={
         'type':4,
         'keyword':'付仲凌'
     }
     r = requests.post(url,data=common.dumps_text(date), headers=headers)
     print(r.json())

 def SupplySaleOrder(self,id): #用户补充
      membertoken=shopkeeper_token
      delivery_no=Common.random_num(5)
      #membertoken = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaDUuc2h1aXhpb25na2VqaS5uZXRcL2FwcFwvTG9naW5CeUg1IiwiaWF0IjoxNTYwOTU0NDM3LCJleHAiOjE1NjA5NjE2MzcsIm5iZiI6MTU2MDk1NDQzNywianRpIjoiY0VvWGRoWFNwZUh3cTU3ciIsInN1YiI6NDgzNDgsInBydiI6IjZkOWJkZjNhOTA1NzZhN2E2MmY4Y2M1ZDJjNWJiNmY4ZWFjYWQ4MTciLCJpZCI6NDgzNDgsInJvbGUiOiJVU0VSIiwiaXNfdXNlciI6dHJ1ZSwicm9sZV9pZCI6MCwicmVzZXRfdGltZSI6IjIwMTktMDYtMTEgMTY6NDI6MDAiLCJvcGVuaWQiOiJvVmtBbzU1UUtQNWJEcklud25oOEZWQTBXcHNRIiwidGhpcmRfcGFydF9pZCI6MzMyNDA5fQ.3qCj4Z4W8Td1I31ZS2pYh1paA_Udy9yhGsnuWhAcpNA'
      url = Common.first_url()+'app/SupplySaleOrder'
      headers = {
          'Content-Type': "application/json",
          'Authorization': membertoken
      }
      date = {
          'id':id,
          'delivery_no':'371422'+delivery_no,
          'delivery_id':75,
          'images':['http://thirdwx.qlogo.cn/mmopen/vi_32/pV00oiasYq7NEJDjSg25yY6LB0pLUmZtcY7RtME5CxCpGYPSNwDGVNkffkRLicygVa8lJoc1kvHZJLB02J9H5cTg/132']
      }
      r = requests.post(url, data=json.dumps(date), headers=headers)
      if r.status_code==200:
          print('用户补充信息:' + '售后id:'+str(id)+' '+str(r.json()))
      else:raise NameError(r.status_code)

 def  Admin_PostSaleOrders(self): #订单状态统计
     token1 = admin_token
     url = Common.first_url()+ 'admin/PostSaleOrders'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }
     r = requests.get(url, headers=headers)
     print(r.json())
 def CreateJobOrder(self):#创建工单
     token1 = admin_token
     url = Common.first_url()+ 'admin/CreateJobOrder'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }
     date={
         'title':'jdiwedw',
         'order_id':503103,
         'type':1,
         #'type_id':1,
         'content':'wdwdfefef',
         'product_images':['51545'],
         'afterSale_images':['4848']
     }

     r = requests.post(url, json.dumps(date),headers=headers)
     print(r.json())

 def  JobOrder(self):#工单列表
     token1 =admin_token
     url =Common.first_url()+ 'admin/JobOrder'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }
     date = {
        'order_id':1374583
     }

     r = requests.get(url, params=date, headers=headers)
     print(r.json())

 def Admin_SaleOrderRefund(self):#售后记录
      token1 =admin_token
      url = Common.first_url()+'admin/SaleOrderRefund'
      headers = {
          # Bearer
          'Content-Type': "application/json",
          'Authorization': token1
          # "cookie": "token="+ membertoken
      }
      r = requests.get(url, headers=headers)
      print(r.json())

 def GetQiYuTemplateField(self):  # 获取七鱼工单模板字段
        token1 =admin_token
        url =Common.first_url()+'admin/GetQiYuTemplateField'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token1
            # "cookie": "token="+ membertoken
        }
        data={
            'templateId':0
        }
        r = requests.get(url,data=data,headers=headers)
        print(r.json())
 def GetQiYuGroup(self):  # 获取七鱼用户组
        token1 = admin_token
        url =Common.first_url()+'admin/GetQiYuGroup'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token1
        }
        # data={
        #     'templateId':0
        # }
        r = requests.get(url,headers=headers)
        print(r.json())
 def GetQiYuGroupMember(self):  # 获取七鱼用户组成员列表
        token1 = admin_token
        url =Common.first_url()+'admin/GetQiYuGroupMember'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token1
            # "cookie": "token="+ membertoken
        }
        data={
            'groupId':1,
            'role':2
        }
        r = requests.get(url,params=data,headers=headers)
        print(r.json())

 def SavePostSaleType(self):  # 修改类型配置
        token1 = admin_token
        url = Common.first_url()+'admin/SavePostSaleType'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token1
            # "cookie": "token="+ membertoken
        }
        data = {
            'id': 7,
            'type_name': '测试154489489989889',
            'sale_type_configs':{'id':4,'config_name':'退商品金额324'}
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r.json())

 def CreatePostSaleType(self):  # 创建类型配置
        token1 = admin_token
        url =Common.first_url()+'admin/CreatePostSaleType'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token1
            # "cookie": "token="+ membertoken
        }
        data = {
            'type_name': '开车',
            'tag_name': '老司机',
            'type':0,
            'menu_id':1012
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r.json())

 def PostSaleType(self):  # 类型配置列表
        token1 = admin_token
        url = Common.first_url()+'admin/PostSaleType'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token1
            # "cookie": "token="+ membertoken
        }
        r = requests.get(url, headers=headers)
        print(r.json())
 def PostSaleTypeDetail(self):#配置类型详情
     token1 = admin_token
     url = Common.first_url()+'admin/PostSaleTypeDetail'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }
     date={
         'id':11,

     }
     r = requests.get(url,params=date,headers=headers)
     print(r.json())


 def SetConfig (self):#售后单自动关闭
     token1 = shopkeeper_token
     url =Common.first_url() + 'app/SetConfig'
     headers = {
         # Bearer
         'Content-Type': "application/json",
         'Authorization': token1
         # "cookie": "token="+ membertoken
     }
     data={
         'ckey':'timeout',
         'cvalue':'2',
         'parent_key':'postSaleOrder.autoClose'
     }
     r=requests.post(url,data=Common.dumps_text(data),headers=headers)
     print(r.json())

 def SingleOrders(self,token,sub_order_id):#签收接口
     url =Common.first_url()+'admin/SingleOrders'
     header = {'Content-Type': 'application/json',
               'Authorization':token

               }
     date = {'sub_order_id': sub_order_id}
     data1 = Common.dumps_text(date)
     req = requests.post(url=url, headers=header, data=data1)
     print('签收：'+str(req.json()))
     # 结算

     # url = 'http://h5.shuixiongkeji.net/admin/CompletedOrders'
     # header = {'Content-Type': 'application/json',
     #           'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaDUuc2h1aXhpb25na2VqaS5uZXRcL2FkbWluXC9BZG1pbkxvZ2luIiwiaWF0IjoxNTYwNTk2MTk4LCJleHAiOjE1NjE4MDU3OTgsIm5iZiI6MTU2MDU5NjE5OCwianRpIjoiVDY5dVQ1c1NCZklBOWxIMyIsInN1YiI6MSwicHJ2IjoiOTcwMzBiM2RiMjQyMDhjNDJkZTcyZmY2NTZjNDcwYWIyMDJmYjlmMCIsInJvbGUiOiJBRE1JTiIsInVzZXJuYW1lIjoic3hraiIsImlkIjoxLCJpc19hZG1pbiI6dHJ1ZSwicm9sZV9pZCI6MSwicmVzZXRfdGltZSI6IjIwMTktMDQtMjcgMjI6NDQ6NDMifQ.YlrdVFsGlJ1IwuUc5Z8PlPvuI6qe7zIt5czYV9ywwWs'
     #           }
     # date = {
     #     'sub_order_id': sub_order_id
     # }
     # data1 = Common.dumps_text(date)
     # req = requests.post(url=url, headers=header, data=data1)
     # print(req.json())
#member().SetConfig()
#member().SupplySaleOrder()
