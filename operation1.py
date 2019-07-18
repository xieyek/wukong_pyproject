# -*- encoding:utf-8 -*-
# 新的运营后台接口
from Common import var
from Common.common import Common
from Common.http_method import Http


class Operation1(object):

    # 发送验证码
    @staticmethod
    def post_sms(token, phone="13725321096", sense=7):
        data = {
            "phone": phone,
            "sense": sense,  # 7设置全球合伙人
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url()+"Sms", data1, token)
        print("发送验证码"+str(obj.status_code))
        Common.out_error(obj)
        return obj

    # 设置为全球合伙人
    @staticmethod
    def post_order(token, member_id, code):
        data = {
            "code": code,
            "member_id": member_id,  # 7设置全球合伙人
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url()+"Orders", data1, token, ant_action="upgradeVip4")
        print("设置为全球合伙人"+str(obj.status_code))
        Common.out_error(obj)
        return obj


    # 获取待审核商品列表
    @staticmethod
    def get_products_list(token, sortedBy="desc", orderBy="id", search="approval_status:0;type:2",
                          searchFields="approval_status:=;type:<", page=1, limit=15,
                     with1="Businesses;BusinessBrands;ProductCategories", searchJoin="and", withType=1):
        data = {
            "sortedBy": sortedBy,
            "orderBy": orderBy,
            "search": search,
            "searchFields": searchFields,
            "page": page,
            "limit": limit,
            "with": with1,
            "searchJoin": searchJoin,
            "withType": withType
        }
        obj = Http.get(Common.first_url()+"Products", data, token)
        print("获取待审核商品列表"+str(obj.status_code))
        Common.out_error(obj)
        return obj

    # 获取指定商品的详情
    @staticmethod
    def get_product_detail(token, product_id, product_sku_id, withSearchFields="ProductAlbums.product_sku_id:=",
                           with1="ProductSkus;ProductDetails;ProductAlbums;productCardExchangePeriod;productType"):
        data = {
            "withSearch": "ProductAlbums.product_sku_id:%s" % product_sku_id,
            "withSearchFields": withSearchFields,
            "with": with1,
        }
        obj = Http.get(Common.first_url()+"Products/{0}".format(product_id), data, token)
        print("获取指定商品的详情"+str(obj.status_code))
        Common.out_error(obj)
        return obj

    # 审核商品
    @staticmethod
    def put_products_audit(token, product_id, factory_price=var.factory_price, Lv1_price=var.Lv1_price, Lv20_price=var.Lv20_price):
        data= {
                "albums": [{
                    "image": "https://mayistatic.bc2c.cn/images/8f95e0d6-852f-4402-bd67-34e0329371a7.jpg",
                    "type": 1
                }, {
                    "image": "https://mayistatic.bc2c.cn/images/50e8b12a-bc33-491a-9088-5c81db4092f5.jpg",
                    "type": 1
                }, {
                    "image": "https://mayistatic.bc2c.cn/images/e059d843-a930-4937-9285-a8d21ed91514.jpg",
                    "type": 1
                }, {
                    "image": "https://mayistatic.bc2c.cn/images/9cd5ac59-7d63-4dd9-a88c-0b65ef0bd118.jpg",
                    "type": 1
                }],
                "content": "<p>商品描述</p>",
                "approval_status": "1",
                "cover": "https://mayistatic.bc2c.cn/images/e2307bd9-7303-4712-9a0a-629058ac04c5.jpg",
                "factory_price": factory_price,
                "is_new": 0,
                "name": "1554630977",
                "original_price": "0.00",
                "purchcase_num": 0,
                "sale_num": 0,
                "sku": [],
                "summary": "商品简介",
                "unit": "商品单位",
                "weight": "1kg",
                "wholesale1_price": Lv20_price,
                "wholesale2_price": Lv1_price,
                "max_limit": "1",
                "min_limit": "1",
                "sale_price": "100000",
                "department_id": 1,
                "short_title": "短标题",
                "daily_category_id": 3

        }
        data1 = Common.dumps_text(data)
        obj = Http.put(Common.first_url() + "Products/{0}".format(product_id), data1, token)
        print("审核商品" + str(obj.status_code))
        Common.out_error(obj)
        return obj

    # 查看今天开的团
    @staticmethod
    def post_DailySales_today(token):
        obj = Http.post(Common.first_url() + "DailySales", None, token, ant_action="dailySelling")
        print("查看今天开的团" + str(obj.status_code))
        Common.out_error(obj)
        return obj

    # 开团
    @staticmethod
    def post_DailySales(token, product_id, price=var.dailysales_price, start_at=Common.current_time()[:10]):

        data = {
            "start_at": start_at,
            "products": [{
                "product_id": product_id,
                "price": price
            }],
            "cover": "https://mayistatic.bc2c.cn/images/fcfc5693-2c3e-4280-97b7-b256585bf868.png"
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "DailySales", data1, token, ant_action="add")
        print("开团" + str(obj.status_code))
        Common.out_error(obj)
        return obj

    # 编辑团
    @staticmethod
    def put_DailySales(token, daily_sales_id, product_id, price=var.dailysales_price, start_at=Common.current_time()[:10]):

        data = {
            "start_at": start_at,
            "products": [{
                "product_id": product_id,
                "price": price
            }],
            "cover": "https://mayistatic.bc2c.cn/images/fcfc5693-2c3e-4280-97b7-b256585bf868.png"
        }
        data1 = Common.dumps_text(data)
        obj = Http.put(Common.first_url() + "DailySales/{0}".format(daily_sales_id), data1, token)
        print("编辑团" + str(obj.status_code))
        Common.out_error(obj)
        return obj


    # 开团
    @staticmethod
    def post_products_search(token):
        data = {
            "business_id": [],
            "isDailySale": 1,
            "keyword": "",
            "page": 1
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "Products", data1, token, ant_action="search")
        print("开团" + str(obj.status_code))
        Common.out_error(obj)
        return obj
