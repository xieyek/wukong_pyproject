from Common.common import Common
from http_method import Http
import  json
import requests
from  sql import Mysql
class showping:
    def indexshowping(self,token,num):
        url=Common.first_url()+'app/MrdGetDailySale'
        headers = {
            'Content-Type': "application/json",
            'Authorization': token
        }
        res=requests.get(url,headers=headers)
        product_id=res.json()['data']['products'][0]['product_id']
        price=res.json()['data']['products'][0]['price']
        id = res.json()['data']['products'][num]['id']# 首页第几个商品，0，1，....
        if(id!=None):
            sql = "SELECT * FROM products WHERE id=%d;" % product_id
            exesql = Mysql().sqlclien(sql)
            businessid = exesql[0][1]
            stock = exesql[0][16]
        else:
            print('悟空团还没有商品')

        if(res.status_code==200):
            print('获取商品成功'+str(res.json()['data']['products'][num]))
            #businessid, stock,
            return id, product_id, price,businessid,stock
        else:
          print('获取商品失败'+str(res.json()))


    #我的订单页面
    def showpinginfo(self,id,token,sku_num=0):
        url=Common.first_url()+'app/DailySaleDetail?id=%d'%id
        headers = {
            'Content-Type': "application/json",
            'Authorization': token
        }
        res=requests.get(url,headers=headers).json()
        daily_sale_id =res['data']['daily_sale_id']
        #总剩余库存
        total_stock = res['data']['stock']

        if (res['data']['buy']['attr'] == []):
            # 单规格库存
            one_sku_stock = res['data']['buy']['default_sku_stock']
            one__sku_id = res['data']['buy']['default_sku_id']
            return daily_sale_id, one__sku_id, total_stock, one_sku_stock
        else:
            # 多规格库存
            moer_sku_stock = res['data']['buy']['sku'][sku_num]['sku_stock']
            moer_sku_stock_id = res['data']['buy']['sku'][sku_num]['sku_id']
            return daily_sale_id,moer_sku_stock_id, total_stock, moer_sku_stock
    def Freights(self,token,product_sku_id):  #运费模版
        url=Common.first_url()+'app/Freights'
        headers = {
            'Content-Type': "application/json",
            'Authorization': token
        }
        data={
            'product_sku_id':product_sku_id,
            'province':'北京市',
            'city':'北京市',
            'area':'东城区'
        }
        data1=Common.dumps_text(data)
        res=requests.get(url,headers=headers,data=data1).json()
        freights_id=res['data']['freights'][0]['template_id']
        return freights_id
