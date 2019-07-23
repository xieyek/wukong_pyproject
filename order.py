from http_method import Http
# from login import Login
from cf import *
import requests
from showping import showping
from sql import Mysql
from Common.common import Common
class order(object):
    def bulidorder(self,token,order_num,product_sku_id,daily_sale_id,is_platform=1): #创建订单
        # product=showping().indexshowping(token,index_num)
        # product_info=showping().showpinginfo(product[0],token)
        # product_sku_id=product_info[1]
        # daily_sale_id=product_info[0]
        freight_template_id= showping().Freights(token,product_sku_id)
        url=Common.first_url()+'app/GenerateDailySaleOrder'
        #url="https://hotfix.shuixiongkeji.net/app/GenerateDailySaleOrder"
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token
            # "cookie": "token="+ membertoken
        }
        data={
            "is_platform": is_platform,
            'area_code':'110101',
            'product_sku_id':product_sku_id,
            'product_num':order_num,#购买数量
            'daily_sale_id':daily_sale_id,
            'contacter':'哈哈哈',
            'province':'北京市',
            'city':'北京市',
            'area':'东城区',
            'address':'Lucie小店区',
            'mobile':'18000000417',
            'remark':'快点发货',
            'freight':"0",
            'freight_template_id':freight_template_id,
            'is_gift':'0',
            'gift_text':'',
            'selected_order_label_array':'0',
            'product_attr_val_id':'0'
        }
        data1 = Common.dumps_text(data)
        order= requests.post(url=url, headers=headers, data=data1).json()
        if order['status']== 200 and is_platform==1:
            print('创建官推商品成功:' + str(order))
            trade_no = order['data']['trade_no']
            short_no = order['data']['short_no']
            pay_price=order['data']['pay_price']
            return trade_no, short_no,order_num,pay_price
        elif order['status']== 200 and is_platform==0:
            print('创建明星掌柜商品成功:' + str(order))
            trade_no = order['data']['trade_no']
            short_no = order['data']['short_no']
            pay_price = order['data']['pay_price']
            return trade_no, short_no, order_num, pay_price
        else:print("创建订单失败",order)
    def payorder(self,token,trade_no): #余额支付
        url=Common.first_url()+'app/PayBySystem'
       # url="https://hotfix.shuixiongkeji.net/app/PayBySystem"
        headers = {
        # Bearer
        'Content-Type': "application/json",
        'Authorization': token
    }
        data={
            'trade_no':trade_no,
            'password':'',
            'sense': '5'
        }
        res=requests.post(url,data=Common.dumps_text(data),headers=headers)
        if(res.json()['status']==200):
         print('支付成功:'+str(res.json()))
        else: print('支付失败:'+str(res.json()))

    def qxzhifuorder(self,token,short_no): #取消已支付订单
        url=Common.first_url()+'app/CancelRetailOrder'
        #url="https://hotfix.shuixiongkeji.net/app/CancelRetailOrder"
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token
            # "cookie": "token="+ membertoken
        }
        data={
            'short_no':short_no
        }
        res=requests.post(url,data=Common.dumps_text(data),headers=headers)
        if (res.json()['status'] == 200):
            print('取消成功:' + res.text)
        else:
            print('取消失败:' + res.text)

        #获取自己的订单
    def myorder(self,token,status=0,page=1,keyword='',limit=15): # status -1全部，-2待付款，0待发货，1已发货待收货，4已完成，5已关闭,想要调用发货函数建议0
            url=Common.first_url()+'app/MrdRetailOrder?status={0}&page={1}&keyword={2}&limit={3}'.format(
                status,page,keyword,limit
            )
            # url='https://hotfix.shuixiongkeji.net/app/MrdRetailOrder?status={0}&page={1}&keyword={2}&limit={3}'.format(
            #     status,page,keyword,limit
            # )
            headers = {
                # Bearer
                'Content-Type': "application/json",
                'Authorization': token
                # "cookie": "token="+ membertoken
            }
            res=requests.get(url,headers=headers).json()
            if(res['data']['data']==[]):
                print('没有数据')
            else:
                # 取到列表第一个商品
                sub_order_id = res['data']['data'][0]['sub_order_id']
                daily_sale_order_short_no = res['data']['data'][0]['daily_sale_order_short_no']
                dailysale_order_price = res['data']['data'][0]['dailysale_order_price']
                #consumer_price=res['data']['data'][0]['products'][0]['consumer_price']
                sql = 'SELECT * FROM sub_orders WHERE id=%d; ' % sub_order_id

                sql_sub_order_id = Mysql().sqlclien(sql)[0][1]
                threa_order_status = 'SELECT d.status,s.status,o.status FROM daily_sale_orders d LEFT JOIN sub_orders s ON d.order_id=s.order_id LEFT JOIN orders o ON d.order_id=o.id WHERE d.order_id=%d;' % sql_sub_order_id
                order_status_total = Mysql().sqlclien(threa_order_status)
                print('商品信息：' + '订单号： ' + str(daily_sale_order_short_no) + '  ' + '价格; ' + str(
                    dailysale_order_price)
                      + ' ' + 'sub_order_status: ' + str(
                    order_status_total[0][1]) + ' ' + 'daily_sale_orders_status: ' + str(
                    order_status_total[0][0]) + ' ' + 'order_status: ' + str(order_status_total[0][2])
                      )
            return sub_order_id, sql_sub_order_id,dailysale_order_price



     #未支付取消订单
    def nopayquxiao(self,token,trade_no):
        url=Common.first_url()+'app/DailySaleOrderCancel'
        #url='https://hotfix.shuixiongkeji.net/app/DailySaleOrderCancel'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token
            # "cookie": "token="+ membertoken
        }
        data = {
            'trade_no': trade_no
        }
        res=requests.post(url,data=Common.dumps_text(data),headers=headers)
        if(res.json()['status']==200):
            print('未支付取消成功:'+ str(res.json()))
        else:
            print('未支付取消失败:'+ str(res.json()))
     #免费支付接口
    def post_daily_sale_order_paid(self,token, trade_no, pay_price):
        data = {
            "trade_no": trade_no,  # 流水账号
            "pay_price": pay_price,  # 支付价格
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "app/DailySaleOrderPaid", data1, token)
        print("创建悟空团订单后虚假支付" + str(obj.json()))
        Common.out_error(obj)
        return obj

    # 创建订单后微信支付
    @staticmethod
    def post_pay_order(token, trade_no, money="26", pay_type="2", sense="5", description="购买团购商品",
                       open_id=openid, is_h5="", return_url=""):
        data = {
            "trade_no": trade_no,  # 流水账号
            "money": money,  # 订单金额
            "pay_type": pay_type,  # 支付方式  2微信
            "sense": sense,  # 5购买团购商品、2购买服务包
            "description": description,  # 购买团购商品、购买服务包
            "open_id": open_id,  # 第一份成为会员时使用，后期买卡不需要
            "is_h5": is_h5,
            "return_url": return_url
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "app/PayOrder", data1, token)
        print("创建订单后微信支付" + str(obj.status_code)+str(obj.json()))
        Common.out_error(obj)
        return obj

    # C端创建悟空团订单
    @staticmethod
    def post_generate_daily_sale_order_C(token, member_id, consumer_id, product_sku_id, product_num, daily_sale_id,
                                         freight_template_id, product_attr_val_id=0, selected_order_label_array=[],
                                         remark="备注", freight=0, contacter="测试收货人", mobile="18928861036",
                                         province="广东省", city="广州市", area="荔湾区", address="沙面南街1号",
                                         area_code="440103", pay_vip=0):
        data = {
            "member_id": member_id,
            "consumer_id": consumer_id,
            "product_sku_id": product_sku_id,  # 产品类型
            "product_num": product_num,  # 下单数量
            "daily_sale_id": daily_sale_id,  # 悟空团的ID
            "freight_template_id": freight_template_id,  # 配送的物流ID
            "product_attr_val_id": product_attr_val_id,  # 商品的属性ID，默认0
            "remark": remark,
            "freight": freight,
            "contacter": contacter,
            "mobile": mobile,
            "province": province,
            "city": city,
            "area": area,
            "address": address,
            "area_code": area_code,
            "selected_order_label_array": selected_order_label_array,
            "pay_vip": pay_vip,  # 默认0
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "app/GenerateDailySaleOrder", data1, token)
        print("C端创建悟空团订单" + str(obj.status_code))
        Common.out_error(obj)
        return obj









