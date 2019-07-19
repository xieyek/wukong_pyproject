from login import Login
from memberinfo import member
from cf import *
from showping import showping
from  order import order
# from login import Login
from business import Business
class UserList(object):
    # 注册悟空掌柜，绑定邀请人购卡刷钱
    @staticmethod
    def register_card_bill():
        token, mobile = Login().unregistered_mobile()
        member().register_shopkeeper(token)

    def order_list(self,order_num,index_num,type=0,SingleOrder=3):
         business = Business()
         product = showping().indexshowping(shopkeeper_token, index_num)
         product_info = showping().showpinginfo(product[0], shopkeeper_token)
         product_sku_id = product_info[1]
         daily_sale_id = product_info[0]
         # freight_template_id = showping().Freights(shopkeeper_token, product_sku_id)
         if type==0:
             bulidorder = order.bulidorder(self,token=shopkeeper_token, order_num=order_num,product_sku_id=product_sku_id,daily_sale_id=daily_sale_id)  # 创建订单
             trade_no = bulidorder[0]
             short_no = bulidorder[1]
             num = bulidorder[2]
             price = bulidorder[3]
             order.payorder(self,token=shopkeeper_token, trade_no=trade_no)  # 余额购买
         if type==1:
             bulidorder = order.bulidorder(self, token=shopkeeper_token, order_num=order_num,
                                           product_sku_id=product_sku_id, daily_sale_id=daily_sale_id)  # 创建订单
             trade_no = bulidorder[0]
             short_no = bulidorder[1]
             num = bulidorder[2]
             price = bulidorder[3]
             order.payorder(self, token=shopkeeper_token, trade_no=trade_no)  # 余额购买
             order_data = order.myorder(self,token=shopkeeper_token)  # 我的订单
             price = order_data[2]
             sub_order_id = order_data[0]
             order_id = order_data[1]
             business.takeshoping(supplier_token, sub_order_id)  # 拣货
             return order_id,price

         if type==2:
             bulidorder = order.bulidorder(self, token=shopkeeper_token, order_num=order_num,
                                           product_sku_id=product_sku_id, daily_sale_id=daily_sale_id)  # 创建订单
             trade_no = bulidorder[0]
             short_no = bulidorder[1]
             express_num = bulidorder[2]
             price = bulidorder[3]
             order.payorder(self, token=shopkeeper_token, trade_no=trade_no)  # 余额购买
             order_data = order.myorder(self, token=shopkeeper_token)  # 我的订单
             price = order_data[2]
             sub_order_id = order_data[0]
             order_id = order_data[1]
             business.takeshoping(supplier_token, sub_order_id)  # 拣货
             res=business.fahuo(supplier_token,short_no, sub_order_id, express_num)  # 发货
             return order_id, price
         if type==3:
             bulidorder = order.bulidorder(self, token=shopkeeper_token, order_num=order_num,
                                           product_sku_id=product_sku_id, daily_sale_id=daily_sale_id)  # 创建订单
             trade_no = bulidorder[0]
             short_no = bulidorder[1]
             express_num = bulidorder[2]
             price = bulidorder[3]
             order.payorder(self, token=shopkeeper_token, trade_no=trade_no)  # 余额购买
             order_data = order.myorder(self, token=shopkeeper_token)  # 我的订单
             price = order_data[2]
             sub_order_id = order_data[0]
             order_id = order_data[1]
             business.takeshoping(supplier_token, sub_order_id)  # 拣货
             res = business.fahuo(supplier_token, short_no, sub_order_id, express_num)  # 发货
             member().SingleOrder(operation_token1, sub_order_id, SingleOrder)  # 签收和完成的
             return order_id, price
    def SaleOrder(self,order_id,price,SaleOrder_type,type=0):
        men=member()
        if type==0:
            SaleOrder_id=men.CreateSaleOrder(order_id,SaleOrder_type,price) #创建售后单
            men.UpdateSaleOrde(operation_token, SaleOrder_id)  # 编辑售后单

        if type==1:
            SaleOrder_id = men.CreateSaleOrder(order_id, SaleOrder_type, price)  # 创建售后单
            men.UpdateSaleOrde(operation_token, SaleOrder_id)  # 编辑售后单
            men.SupplySaleOrder(SaleOrder_id)#用户补充

        if type==2:
            SaleOrder_id = men.CreateSaleOrder(order_id, SaleOrder_type, price)  # 创建售后单
            men.UpdateSaleOrde(operation_token, SaleOrder_id)  # 编辑售后单
            men.SupplySaleOrder(SaleOrder_id)  # 用户补充
            men.SaleOrderHandle(int(SaleOrder_id), 3)  # 审核

        if type==3:
            SaleOrder_id = men.CreateSaleOrder(order_id, SaleOrder_type, price)  # 创建售后单
            men.UpdateSaleOrde(operation_token, SaleOrder_id)  # 编辑售后单
            men.SupplySaleOrder(SaleOrder_id)  # 用户补充
            men.SaleOrderHandle(int(SaleOrder_id), 3)  # 审核
            men.SaleOrderClose(int(SaleOrder_id), price)  # 结案







