from http_method import Http
# from login import Login
import requests
from showping import showping
from sql import Mysql
from Common.common import Common
class order(object):
    def bulidorder(self,token,order_num,product_sku_id,daily_sale_id): #创建订单
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
        if (order['status']== 200):
            print('创建成功:' + str(order))
            trade_no = order['data']['trade_no']
            short_no = order['data']['short_no']
            pay_price=order['data']['pay_price']
            return trade_no, short_no,order_num,pay_price
        else:
            print('创建失败:' + str(order))
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












