import json
import requests
from http_method import Http
import json
from Common.common import Common
from order import order
from cf import *
from sql import Mysql
class Business:
   # token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaG90Zml4LnNodWl4aW9uZ2tlamkubmV0XC9CdXNpbmVzc0F1dGhzIiwiaWF0IjoxNTU5MjIxMzAwLCJleHAiOjE1NjA0MzA5MDAsIm5iZiI6MTU1OTIyMTMwMCwianRpIjoiUXZQYWZ2Wm4xNm15QjdTbyIsInN1YiI6MTU3LCJwcnYiOiI0ODUwNjU3NzNkMTUwMzRkNDI1NWFmNjM0MDMxYTRkMmM0MmE1NTRlIiwiaWQiOjE1Nywicm9sZSI6IkJVU0lORVNTIiwiYWNjb3VudF9pZCI6MTUyLCJyZXNldF90aW1lIjpudWxsLCJyb2xlX2lkIjoxNTIsImlzX2J1c2luZXNzIjp0cnVlLCJidXNpbmVzc19pZCI6MTU3fQ.GhU91s55855YDBdIvBkLMg4N12e38fXxdt1QPNfmMpI'
    def takeshoping(self,token,sub_order_id):
        url=Common.first_url()+'seller/CheckedOrders'
        #url='https://hotfix.shuixiongkeji.net/SubOrders?'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token
            # "cookie": "token="+ membertoken
        }
        data={
            "sub_order_id": sub_order_id
        }
        data1 = json.dumps(data)
        res = requests.post(url, data1, headers=headers)
        if(res.status_code==200):
            print('拣货成功:'+str(res.json()))
        else:
            print('拣货失败:'+str(res.json()))


    def fahuo(self,token,short_no,sub_order_id,express_num):
        url=Common.first_url()+'seller/UnifyDeliverGoods'
        #url='https://hotfix.shuixiongkeji.net/OrderExpresses?'
        headers = {
            # Bearer
            'Content-Type': "application/json",
            'Authorization': token
            # "cookie": "token="+ membertoken
        }
        data={"orders":[{"delivery_name":"申通快递",
                         "delivery_no":"3714219852419",
                         "short_no":short_no,
                         "sub_order_id":sub_order_id,
                         "express_num":express_num}]}
        data1 = json.dumps(data)
        res=requests.post(url,data1,headers=headers)
        #res = Http.post(url, data1, token)
        if (res.status_code == 200):
            print('发货信息'+str(res.json()))
            return res.status_code
        else:
            print('发货信息'+str(res.json()))
        sql = 'SELECT * FROM sub_orders WHERE id=%d; ' % sub_order_id
        sql_sub_order_id = Mysql().sqlclien(sql)[0][1]
        threa_order_status = 'SELECT d.status,s.status,o.status FROM daily_sale_orders d LEFT JOIN sub_orders s ON d.order_id=s.order_id LEFT JOIN orders o ON d.order_id=o.id WHERE d.order_id=%d;' % sql_sub_order_id
        order_status_total = Mysql().sqlclien(threa_order_status)
        print( 'sub_order_status: ' + str(
            order_status_total[0][1]) + ' ' + 'daily_sale_orders_status: ' + str(
            order_status_total[0][0]) + ' ' + 'order_status: ' + str(order_status_total[0][2])
              )
    #添加商品
    def post_products_keyattr(self,token, product_category_id=2, name="洗面奶111",
                                      factory_price='10', sale_price='20', weight="1kg",
                                      unit="个", content="111111",
                                      product_attr_keys_id=None, product_attr_attr_id=None, product_attr_keys_name=None,
                                      product_attr_attr_name=None,
                                      stock="100", sku="", sku_status=1, freight_template=[],
                                      product_attr_key=[],
                                      approval_status=0, status=0, type=0,
                                      cover="https://mayistatic.bc2c.cn/images/b56df393-0d64-4181-a59d-53f207df80eb.jpg",
                                      size_img="https://mayistatic.bc2c.cn/images/2d461022-3aee-4be8-95a8-dbc3d5ddb99a.jpg",
                                      license_img= "https://mayistatic.bc2c.cn/images/2d461022-3aee-4be8-95a8-dbc3d5ddb99a.jpg"):

                url='https://hotfix.shuixiongkeji.net/Products'
                data = {
                    "cover": "https://mayistatic.bc2c.cn/images/b56df393-0d64-4181-a59d-53f207df80eb.jpg",
                    "name": "洗面奶",
                    "product_category_id": 2,
                    "approval_status": 0,
                    "status": 0,
                    "type": 0,
                    "sku": [{
                        "stock": "50",
                        "sku": "",
                        "status": 1,
                        "factory_price": "10",
                        "sale_price": "20"
                    }],
                    "albums": [],
                    "content": "<p>1111111</p>",
                    "weight": "1kg",
                    "unit": "个",
                    "freight_template": [],
                    "sku_attr_val_image": [],
                    "license_img": "[]",
                    "size_img": "[\"https://mayistatic.bc2c.cn/images/2d461022-3aee-4be8-95a8-dbc3d5ddb99a.jpg\"]",
                    "product_attr_key": []
                }
                data1 = json.dumps(data)
                obj = Http.post(url, data1, token)
                print("添加指定规格的商品" + str(obj.json()))
                return obj






