import json
import time

import requests

import cf
import var
from http_method import Http
import json
from Common.common import Common
from order import order
from cf import *
from sql import Mysql
class Business(object):
    # 获取验证码
    def post_GetVerifyCode(self,token, phone=13538997357):
        data = {"phone": phone, "sense": 8}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "seller/GetVerifyCode", data1, token)
        print("获取验证码" + str(obj.status_code))
        Common.out_error(obj)
        return obj
    # 添加供应商售后地址
    def post_ProductAfterSale(self,token, code, mobile=13538997357):
        data = {"contacts": "花猪", "logistics": "顺丰", "mobile": mobile, "telephone": "", "code": code, "area": 4648,
                "address": "圣诞节开发"}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "seller/ProductAfterSale", data1, token)
        print("添加供应商售后地址" + str(obj.status_code))
        Common.out_error(obj)
        return obj
    #拣货
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

    # 添加默认规格的商品
    @staticmethod
    def post_products(token, product_after_sale_id, product_category_id=2, name="专用枕头",
                          factory_price=var.factory_price, sale_price=var.sale_price, content="商品描述",
                          stock="1000000", sku="", sku_status=1, freight_template=[], approval_status=0, status=0,
                          type=0,
                          sku_attr_val_image=[], cover="https://mayistatic.bc2c.cn/FtuiEMOuduOnpuiE3r_m7OMor-Fa?imageMogr2/auto-orient", albums=[],
                          size_img='["https://mayistatic.bc2c.cn/FjsFdrNBnaKiGlh_hMOFGimw_Np_?imageMogr2/auto-orient"]',
                          license_img='["https://mayistatic.bc2c.cn/FlEyyzSGBd_RgU7briPkn7HF5wVq?imageMogr2/auto-orient"]',
                          product_attr_key=[], is_draft=0):
            data = {
                "product_category_id": product_category_id,  # 商品分类ID
                "name": name,  # 商品名称
                "cover": cover,  # 商品封面
                "albums": albums,  # 附图。可为空
                "content": "<p>%s</p>" % content,
                "size_img": size_img,  # 规格参数对照图
                "license_img": license_img,  # 相关资质
                "factory_price": factory_price,  # 工厂价/商品价
                "sku": [{
                    "stock": stock,  # 商品一个规格的库存
                    "sku": sku,
                    "status": sku_status,  # 默认1
                    "factory_price": factory_price,  # 工厂价/商品价
                    "sale_price": sale_price,  # 零售价
                }],
                "freight_template": freight_template,  # 运费模板:格式[1, 2, 4]
                "approval_status": approval_status,  # 审核状态 0-等待审核 1-通过 2-不通过
                "status": status,  # 状态 0-下架 1-上架
                "type": type,  # 类型 0-实体商品 1-虚拟商品 2-会员卡
                "sku_attr_val_image": sku_attr_val_image,
                "product_attr_key": product_attr_key,
                'product_after_sale_id': product_after_sale_id,
                'is_draft': is_draft
            }
            data1 = Common.dumps_text(data)
            obj = Http.post(Common.first_url() + "Products", data1, token)
            print("添加默认规格的商品" + str(obj.status_code))
            Common.out_error(obj)
            return obj

     # 默认规格商品规格审核
    @staticmethod
    def post_ProductSpecAudit(token, product_id, approval_status=1, approval_reason='',
                              size_img="[\"https://mayistatic.bc2c.cn/FjsFdrNBnaKiGlh_hMOFGimw_Np_?imageMogr2/auto-orient\"]"):
        data = {"product_id": product_id,
                "approval_status": approval_status,
                "approval_reason": approval_reason,
                "size_img": size_img}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/ProductSpecAudit", data1, token)
        print("商品规格审核" + str(obj.status_code))
        Common.out_error(obj)
        return obj

    @staticmethod
    def post_ProductFreightAudit(token, product_id, approval_status=1, approval_reason=''):
        data = {"product_id": product_id,
                "approval_status": approval_status,
                "approval_reason": approval_reason}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/ProductFreightAudit", data1, token)
        print("商品邮费模板审核" + str(obj.status_code))
        Common.out_error(obj)
        return obj

        # 默认规格商品资质审核

    @staticmethod
    def post_ProductLicenseAudit(token, product_id, approval_status=1, approval_reason='',
                                 license_img="[\"https://mayistatic.bc2c.cn/FlEyyzSGBd_RgU7briPkn7HF5wVq?imageMogr2/auto-orient\"]"):
        data = {"product_id": product_id,
                "approval_status": approval_status,
                "approval_reason": approval_reason,
                "license_img": license_img}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/ProductLicenseAudit", data1, token)
        print("商品资质审核" + str(obj.status_code))
        Common.out_error(obj)
        return obj
        # 默认规格完成审核

    def post_CompleteAudit(token, product_id):
        data = {"product_id": product_id}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/CompleteAudit", data1, token)
        print("商品完成审核" + str(obj.status_code))
        Common.out_error(obj)
        return obj


    #默认规格商品填写开团价
    @staticmethod
    def post_ProductPricing(token,product_id,sku_id,sale_price=var.sale_price,daily_sale_price=var.dailysales_price,wholesale1_price=var.Lv20_price,wholesale2_price=var.Lv1_price,approval_status=1,with_product_id=[]):
        data={"product_id": product_id,
              "approval_status": approval_status,
              "with_product_id": with_product_id,
              "sku": [{
                  "sku_id": sku_id,
                  "sale_price": sale_price,
                  "daily_sale_price": daily_sale_price,
                  "wholesale1_price":wholesale1_price,
                  "wholesale2_price": wholesale2_price}]}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/ProductPricing", data1, token)
        print("商品完成审核填写开团价" + str(obj.status_code))
        Common.out_error(obj)
        return obj
     # 审核单规格商品
    @staticmethod
    def CompleteAudit(product_id=''):
        if product_id == '':
            su_token = cf.supplier_token
            # 供应商添加商品
            obj = Business().post_GetVerifyCode(token=su_token, phone=18928803919)
            code = obj.json()['data']['content']
            time.sleep(3)
            obj = Business().post_ProductAfterSale(token=su_token, code=code, mobile=18928803919)
            product_after_sale_id = obj.json()['data']['id']
            p = Business.post_products(su_token, freight_template=[1], product_after_sale_id=product_after_sale_id)
            product_id = Common.loads_text(p)["data"][0]["attributes"]["id"]
        token2 = cf.operation_token1
        obj = Business.get_product_info(token=token2, product_id=product_id)
        sku_id = obj.json()['data']['sku'][0]['id']
        Business.post_ProductInfoAudit(token=token2, product_id=product_id, approval_status=1, approval_reason='',
                                        name="专用枕头", short_title='专用枕头', contrast_url='', daily_category_id=7,
                                        department_id=12)
        Business.post_ProductSpecAudit(token=token2, product_id=product_id)
        Business.post_ProductFreightAudit(token=token2, product_id=product_id)
        Business.post_ProductLicenseAudit(token=token2, product_id=product_id)
        Business.post_CompleteAudit(token=token2, product_id=product_id)
        time.sleep(1)
        Business.post_ProductPricing(token=token2, product_id=product_id, sku_id=sku_id)
        return product_id

        # 获取产品详情

    @staticmethod
    def get_product_info(token, product_id):
        data = {
            "product_id": product_id
        }
        obj = Http.get(Common.first_url() + "admin/ProductInfo", data, token)
        print("获取产品详情" + str(obj.status_code))
        Common.out_error(obj)
        return obj
        # 默认规格商品信息审核

    @staticmethod
    def post_ProductInfoAudit(token, product_id, approval_status=1, approval_reason='', name="小蜜蜜", short_title='小蜜蜜',
                              contrast_url='', daily_category_id=7, department_id=12):
        data = {"product_id": product_id,
                "approval_status": approval_status,  # 为1审核通过为0审核不通过
                "approval_reason": approval_reason,
                "name": name,
                "short_title": short_title,
                "contrast_url": contrast_url,
                "daily_category_id": daily_category_id,
                "department_id": department_id,
                "albums": [{
                    "image": "https://mayistatic.bc2c.cn/FlEyyzSGBd_RgU7briPkn7HF5wVq?imageMogr2/auto-orient",
                    "type": 1,
                    "name": ""
                }],
                "cover": "https://mayistatic.bc2c.cn/FtuiEMOuduOnpuiE3r_m7OMor-Fa?imageMogr2/auto-orient",
                "content": "<p>商品描述</p>"}
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/ProductInfoAudit", data1, token)
        print("商品信息审核" + str(obj.status_code))
        Common.out_error(obj)
        return obj
        # 获取悟空团管理列表
    @staticmethod
    def get_daily_sales(token, start_at=Common.current_time()[:10], end_at=None, page=1, pageSize=15, order="desc",
                        orderField=None,
                        isDailySale=None, status=None, product_name=None, approval_status=None):
        data = {
            "start_at": start_at,  # 开团时间格式：2019-3-28，默认今天
            "end_at": end_at,
            "page": page,
            "pageSize": pageSize,
            "order": order,
            "orderField": orderField,
            "isDailySale": isDailySale,  # 悟空团编辑时调用，值是1
            "status": status,
            "product_name": product_name,
            "approval_status": approval_status
        }
        obj = Http.get(Common.first_url() + "admin/DailySales", data, token)
        print("获取悟空团管理列表" + str(obj.status_code))
        Common.out_error(obj)
        return obj
        # 添加悟空团
    @staticmethod
    def post_daily_sale_create(token, start_at=Common.current_time()[:10], product_id=None,
                               cover="https://mayistatic.bc2c.cn/FtuiEMOuduOnpuiE3r_m7OMor-Fa?imageMogr2/auto-orient"):
        data = {
            "start_at": start_at,  # 开团日期格式："2019-03-29",
            # 参团商品,最多六件
            "products": [{
                "product_id": product_id}],
            "cover": cover,  # 悟空团分享主图:
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/DailySaleCreate", data1, token)
        print(obj.json())
        print("添加悟空团" + str(obj.status_code))
        Common.out_error(obj)
        return obj


    # 编辑团,添加新产品单规格
    @staticmethod
    def modify_dailysale(op_token, daily_sales_id, product_list, product_id,start_at=Common.current_time()[:10]):
        products = [{"product_id": product_id}]
        if len(product_list) <= 4:
            for i in product_list:
                products.append({"product_id": i["product_id"]})
                # sku=[]
                # for sk in i["product_skus"]:
                #     sku.append({"price": sk["price"], "sku_id": sk["sku_id"]})
                # products.append({"product_id": i["product_id"], "sku": sku})
        else:
            for i in product_list[:4]:
                # sku = []
                # for sk in i["product_skus"]:
                #     sku.append({"price": sk["price"], "sku_id": sk["sku_id"]})
                products.append({"product_id": i["product_id"]})
        data = {
            "id": daily_sales_id,
            "start_at": start_at,
            "products": products,
            "cover": "https://mayistatic.bc2c.cn/FtuiEMOuduOnpuiE3r_m7OMor-Fa?imageMogr2/auto-orient"
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "admin/DailySaleUpdate", data1, op_token)
        print("编辑团" + str(obj.status_code))
        Common.out_error(obj)
        return obj


    # 添加商品》商品审核》开团 单规格商品
    @staticmethod
    def product_audit_dailysale(start_at=Common.current_time()[:10]):
        op_token = cf.operation_token1
        su_token = cf.supplier_token
        # 供应商添加商品

        obj = Business().post_GetVerifyCode(token=su_token, phone=19986415739)
        code = obj.json()['data']['content']
        time.sleep(3)
        obj = Business().post_ProductAfterSale(token=su_token, code=code, mobile=19986415739)
        product_after_sale_id = obj.json()['data']['id']
        p = Business.post_products(su_token, freight_template=[1,2], product_after_sale_id=product_after_sale_id)
        product_id = Common.loads_text(p)["data"][0]["attributes"]["id"]

        # 运维审核通过
        Business.CompleteAudit(product_id)
        # 运维获取悟空团列表
        w = Business.get_daily_sales(op_token)
        # print(int(Common.loads_text(w)["data"]["today"])+type(Common.loads_text(w)["data"]["today"]))
        if Common.loads_text(w)["data"]["today"] == []:
            # 运维添加拼团
            Business.post_daily_sale_create(op_token, product_id=product_id,start_at=start_at)
        else:
            daily_sale_id = Common.loads_text(w)["data"]["today"]["id"]
            # 运维修改拼团
            product_list = Common.loads_text(w)["data"]["today"]["products"]
            Business.modify_dailysale(op_token, daily_sale_id, product_list, product_id)
        # 运维获取悟空团列表
        w = Business.get_daily_sales(op_token)
        product_id=Common.loads_text(w)["data"]["today"]["products"][0]['id']
        return product_id





