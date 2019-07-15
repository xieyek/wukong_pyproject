import threading
import time
from cf import *
from showping import showping
from  order import order
from memberinfo import member
from time import ctime
from business import Business
import requests
membertoken=shopkeeper_token
businesstoken=supplier_token
admin_token=operation_token
order = order()
memberinfo=member()
class MyThread(threading.Thread):
    a=0
    def __init__(self):
        super(MyThread, self).__init__()  # 重构run函数必须要写
    def run(self):
        bulidorder = order.bulidorder(membertoken, 1, 2)  # 创建订单
        # trade_no = bulidorder[0]
        # short_no = bulidorder[1]
        # nun = bulidorder[2]
        # pyorder = order.payorder(membertoken, trade_no)  # 余额购买
        #
        # # qxzhifuorder=order.qxzhifuorder(membertoken,short_no) # 取消已支付订单
        # # s=order.nopayquxiao(membertoken,trade_no)
        #
        # order_data = order.myorder(membertoken)  # 我的订单
        # price = order_data[2]
        # sub_order_id = order_data[0]
        # order_id = order_data[1]
        # businessadmin = Business()
        # take = businessadmin.takeshoping(businesstoken, order_id)  # 拣货
        # fahuo = businessadmin.fahuo(businesstoken, membertoken, short_no, sub_order_id, nun)  # 发货
        # # # # sub_order_id=2677894
        # memberinfo.SingleOrders(admin_token, sub_order_id)  # 签收
        # # # # sub_order_id=2684654
        # # # SaleOrder_id='527'
        # SaleOrder_id = memberinfo.CreateSaleOrder(sub_order_id, price, 2)  # 创建售后单
        # memberinfo.SupplySaleOrder(SaleOrder_id)  # 用户补充




if __name__ == "__main__":
    for a in range(5):
        for i in range(2):
            i= MyThread()
            i.start()
        time.sleep(1)
    print('----------------------')

