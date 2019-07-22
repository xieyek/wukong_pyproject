
from time import sleep
import var
import requests
import json
from datetime import *
from http_method import Http
from Common.common import Common
from sql import Mysql
from cf import *
import cf
from operation1 import Operation1
from business import Business
import math
H5_url='http://h5.shuixiongkeji.net/'
admin_token=operation_token
common=Common()
class member():
 def userinfo(self,token):
        url=Common.first_url()+'app/MrdMemberInfo'
        #url = "https://hotfix.shuixiongkeji.net/app/MrdMemberInfo"
        headers = {
            'Content-Type': "application/json",
            'Authorization': token
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
 #绑定邀请人
 def post_update_info(self,token, recommend_code):
     data = {
         "recommend_code": recommend_code,
     }
     data1 = Common.dumps_text(data)
     obj = Http.post(Common.first_url() + "app/UpdateInfo", data1, token)
     print("绑定邀请人手机" + str(obj.status_code)+str(obj.json()))
     Common.out_error(obj)
     return obj
 #实名认证
 def post_member_update(self,token, member_id, realname="真实姓名", license_code="441422199304103302", is_license="1", license_type="1",
                           license_img_back="https://mayistatic.bc2c.cn/Fugt_Cv1_C61HpzjGnyva9VLy8xu?imageMogr2/auto-orient",
                        license_img_front="https://mayistatic.bc2c.cn/FoGxj_MzoLpcXNxdxtWf5XVSwo5s?imageMogr2/auto-orient"):
        data = {
            "id": member_id,
            "is_license": is_license,
            "license_code": license_code,
            license_img_back: license_img_back,
            license_img_front: license_img_front,
            "license_type": license_type,
            "realname": realname
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/MemberUpdate", data1, token)
        print("掌柜实名认证" + str(obj.status_code)+str(obj.json()))
        Common.out_error(obj)
        return obj
        # 创建购买会员卡订单

 #创建购买会员卡订单
 def post_generate_buy_card_order(self,token, membership_card_number=1, type1=0, agent_level_id=None):
     data = {
         "membership_card_number": membership_card_number,  # 购买数量
         "type": type1,  # 类型 0-主动 1-被动
         "agent_level_id": agent_level_id,
     }
     data1 = Common.dumps_text(data)
     obj = Http.post(Common.first_url() + "app/GenerateBuyCardOrder", data1, token)
     print("创建购买会员卡订单" + str(obj.status_code))
     Common.out_error(obj)
     return obj

 # 获取悟空掌柜小店经营权信息
 def get_member_info(self,token):
     obj = Http.get(Common.first_url() + "app/MemberInfo", None, token)
     print("获取悟空掌柜小店经营权信息" + str(obj.status_code)+str(obj.json()))
     Common.out_error(obj)
     return obj

#订单免支付接口
 def post_daily_sale_order_paid(self, token, trade_no, pay_price):
     data = {
         "trade_no": trade_no,  # 流水账号
         "pay_price": pay_price,  # 支付价格
     }
     data1 = Common.dumps_text(data)
     obj = Http.post(Common.first_url() + "app/DailySaleOrderPaid", data1, token)
     print("创建悟空团订单后虚假支付" + str(obj.json()))
     Common.out_error(obj)
     return obj
     # 创建会员卡订单后虚假支付


 def post_member_card_order_paid(self,token, trade_no, pay_price):
     data = {
         "trade_no": trade_no,  # 流水账号
         "pay_price": pay_price,  # 支付价格
     }
     data1 = Common.dumps_text(data)
     obj = Http.post(Common.first_url() + "app/MemberCardOrderPaid", data1, token)
     print("创建会员卡订单后虚假支付" + str(obj.status_code)+str(obj.json()))
     Common.out_error(obj)
     return obj

     # 新增商品加入档期信息接口
 @staticmethod
 def post_AddProductTerm(token, product_id, start_at=Common.current_time()[:10], end_at=Common.next_time(10),
                         stock_warning=300, type=1, type_name='自选'):
     data = {
         "product_id": product_id,
         "start_at": start_at,
         "end_at": end_at,
         'stock_warning': stock_warning,
         'selection_labels': [{'type': type, 'type_name': type_name}]  # type 1为自选 2为新品
     }
     data1 = Common.dumps_text(data)
     obj = Http.post(Common.first_url() + "admin/AddProductTerm", data1, token)
     print("商品加入档期" + str(obj.status_code)+str(obj.json()))
     Common.out_error(obj)
     return obj

 # 升级明星掌柜
 @staticmethod
 def post_MemberUpdate(token, id,is_star=1):
        data= {"id": id,"is_star": is_star}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/MemberUpdate", data1, token)
        print("升级明星掌柜" + str(obj.status_code)+str(obj.json()))
        Common.out_error(obj)
        return obj
  #视频关联商品
 @staticmethod
 def post_MemberVideoAdd(token, product_id, member_id, url='https://mayistatic.bc2c.cn/lj735VBrApe0xjjm94VKP3cQ8q0U',
                            cover='https://ws1.sinaimg.cn/large/006c53jqgy1g3o387q7llj303d04h3yc.jpg', width=100, height=300,size=0,status=1):
        data = {
            "product_id": product_id,
            "member_id": member_id,
            "url": url,
            'cover':cover,
            "width": width,
            "height": height,
            "size": size,
            'status': status
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/MemberVideoAdd", data1, token)
        print("视频关联商品" + str(obj.status_code)+str(obj.json()))
        Common.out_error(obj)
        return obj

 # 视频列表

 @staticmethod
 def get_MemberVideo(token):
     obj = Http.get(
         Common.first_url() + "admin/MemberVideo?product=&member_name=&member_bobile=&startTime=&endTime=&is_hidden=&page=1&pageSize=15&orderType=DESC&orderField=id",
         None, token)
     print("获取视频列表" + str(obj.status_code)+str(obj.json()))
     Common.out_error(obj)
     return obj

 #明星掌柜商品绑定
 @staticmethod
 def star_bussiness(member_id,type,product_id=''):
    if product_id=='':
        #添加商品审核
        product_id=Business.CompleteAudit(product_id='')
        #添加到自选池
        member.post_AddProductTerm(type=type,token=cf.operation_token1, product_id=product_id)
        member.post_MemberUpdate(token=cf.operation_token1, id=member_id,is_star=1)
        #绑定视频
        member.post_MemberVideoAdd(token=cf.operation_token1, product_id=product_id, member_id=member_id)
        #获取视频列表
        obj=member.get_MemberVideo(token=cf.operation_token1)
        id=obj.json()['data']['data'][0]['id']
        #返回商品id，视频id
    return product_id,id

 # 注册悟空掌柜，绑定邀请人
 def register_shopkeeper(self,token, recommend_mobile=recommend_mobile):
     # 创建购买会员卡订单,1张
     b = member().post_generate_buy_card_order(token)
     trade_no =Common.loads_text(b)["data"]["trade_no"]
     pay_price =Common.loads_text(b)["data"]["pay_price"]
     # # 创建订单后微信支付
     # ShopKeeper.post_pay_order(token, trade_no, "365", "2", "2", "购买服务包")
     # # 创建订单后微信支付验证支付状态
     # ShopKeeper.post_pay_status(token, trade_no, "2", "2")
     # 创建订单后虚假支付
     member().post_member_card_order_paid(token, trade_no, pay_price)
     # 绑定邀请人
     member().post_update_info(token, recommend_mobile)
     # 获取悟空掌柜小店经营权信息
     m = member().get_member_info(token)
     member_info =Common.loads_text(m)["data"]["id"]
     # 实名认证
     member().post_member_update(operation_token1, member_info)
    # 绑定邀请人手机后激活掌柜权限
    #  member().post_js_signature(token)
     # 获取我的业绩中心信息
     member().get_mrd_order_income(shopkeeper_token)

     # 一键开启小店创建分享链接
 def post_js_signature(self,token, page="wukong_index", url="https://bh5.shuixiongkeji.net/H5/#/index/home"):
     data = {
         "page": page,
         "url": url,
     }
     data1 = Common.dumps_text(data)
     obj = Http.post(Common.first_url() + "app/JsSignature", data1, token)
     print("一键开启小店创建分享链接" + str(obj.status_code))
     Common.out_error(obj)
     return obj

     # 获取我的业绩中心信息
 def get_mrd_order_income(self,token):
     obj = Http.get(Common.first_url() + "app/MrdOrderIncome", None, token)
     print("获取我的业绩中心信息" + str(obj.status_code)+str(obj.json()))
     Common.out_error(obj)
     return obj

  # 购买会员卡 升级或注册

 def buy_member_card(self,token, card_number=1, type1=0):
        if card_number == 0:
            print("购买0张卡")
        elif card_number == var.card_price[4][0]:
            member().global_partner(token)
        else:
            # 创建购买会员卡订单
            if card_number == var.card_price[1][0]:
                o = member().post_generate_buy_card_order(token, card_number, type1=type1, agent_level_id=2)
            elif card_number == var.card_price[2][0]:
                o = member().post_generate_buy_card_order(token, card_number, type1=type1, agent_level_id=3)
            elif card_number == var.card_price[3][0]:
                o = member().post_generate_buy_card_order(token, card_number, type1=type1, agent_level_id=4)
            else:
                o = member().post_generate_buy_card_order(token, card_number, type1=type1, agent_level_id=None)
            d = Common.loads_text(o)

            trade_no = d["data"]["trade_no"]
            pay_price = d["data"]["pay_price"]
            # 创建订单后虚假支付
            member().post_member_card_order_paid(token, trade_no, pay_price)
            return trade_no, pay_price
        # 设置为全球人

 def global_partner(self,sp_token):
     op_token = cf.operation_token.operation_token
     # 发送验证码
     c = Operation1.post_sms(op_token, cf.operation_mobile, "7")
     code = Common.loads_text(c)["data"][0]["attributes"]["content"]
     # c = Operation.get_agent_top_msm(op_token)
     # code = Common.loads_text(c)["data"]["content"]
     # 获取小店经营中心信息
     m = member().get_mrd_member_info(sp_token)
     member_id = Common.loads_text(m)["data"]["id"]
     # 设置全球合伙人
     Operation1.post_order(op_token, member_id, code)
     # Operation.post_set_agent_top(op_token, code, member_id)
     # Common.strike_n(65)

     # 获取小店经营中心信息

 def get_mrd_member_info(self,token):
         obj = Http.get(Common.first_url() + "app/MrdMemberInfo", None, token)
         print("获取小店经营中心信息" + str(obj.status_code))
         Common.out_error(obj)
         return obj


 def CreateSaleOrder(self,sub_order_id,sale_type,price): #创建售后单
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
         'sale_problem_id': 1,
         'sale_type':sale_type,
         'problem_remark': '哈哈哈',
         'number': 1,
         'operator_action':'客服备注',
         'business_duty':0,
         'pay_data':[
                      {'pay_data_id': 1, 'money':price},
              #             {'pay_data_id': 2, 'money': '0.01'},
              # {'pay_data_id': 3, 'money': '0.01'}
                     ],
         "images": [],
         "video": [],
         "product_detail": "",
         "receiver_name": "哈哈哈",
         "receiver_mobile": "18000000417",
         "receiver_province": "北京市",
         "receiver_city": "北京市",
         "receiver_area": "东城区",
         "receiver_address": "Lucie小店区"
     }
     r=requests.post(url,data=common.dumps_text(data),headers=headers)
     if r.json()['status']==200:
         print('创建售后订单信息：' + str(r.json()))
         return r.json()['data']['id']
     else:print('创建售后订单报错信息',r.json())
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
             #  {'pay_data_id': 2,'money': '10'},
             #          {'pay_data_id': 3,  'money': '0.01'}
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
          # 'delivery_no': '3714820492928',
          'delivery_id':75,
          'remark':'哈哈哈',
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
 def UpdateSaleOrde(self,token,id):   #修改售后单
      url = Common.first_url() + 'admin/UpdateSaleOrder'
      headers = {'Content-Type': 'application/json',
                'Authorization': token
                }
      data={
         'id':id,
          'sale_problem_id':1,
          'problem_remark':'哈哈哈哈哈哈',
          'number':1,
          'business_duty':1

     }
      r = requests.post(url, data=Common.dumps_text(data), headers=headers).json()
      print('修改售后信息',r)

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
 def SingleOrder(self,token,sub_order_id, type):
         # 签收
         if type == 1:
             url = Common.first_url()+'admin/SingleOrders'
             header = {'Content-Type': 'application/json',
                       'Authorization': token

                       }
             date = {'sub_order_id': sub_order_id}
             data1 = Common.dumps_text(date)
             req = requests.post(url=url, headers=header, data=data1)
             print(req.json())

         # # 结算
         # #
         if type == 2: #直接完成
             url =Common.first_url()+'admin/CompletedOrders'
             header = {'Content-Type': 'application/json',
                       'Authorization':token
                       }
             date = {
                 'sub_order_id': sub_order_id
             }
             data1 = Common.dumps_text(date)
             req = requests.post(url=url, headers=header, data=data1)
             print(req.json())
         if type == 3: #签收并且完成
             url = Common.first_url()+'admin/SingleOrders'
             url1=Common.first_url()+'admin/CompletedOrders'
             header = {'Content-Type': 'application/json',
                       'Authorization':token
                       }
             date = {
                 'sub_order_id': sub_order_id
             }
             data1 = Common.dumps_text(date)
             req = requests.post(url=url, headers=header, data=data1)
             sleep(0.1)
             res=requests.post(url=url1, headers=header, data=data1)
             print('签收：',req.json())
             print('完成：',res.json())




#member().SetConfig()
#member().SupplySaleOrder()
