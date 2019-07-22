from userList import UserList
from business import Business
from memberinfo import member
#添加商品审核且开团
# product_id=Business.product_audit_dailysale()
#升级明星掌柜并且绑定视频
product_id1,id=member.star_bussiness(member_id=60930,type=1,product_id='')

#绑定邀请人购卡刷钱
# UserList.register_card_bill()

#下单以及拣货，发货，签收
#第一个购买数量，第二个是悟空图第几个商品，第三个是类型:0仅下单并且支付，1，下单且拣货，2.下单且发货，3，下单直到签收完成，第四个默认3
# order_id, price=UserList().order_list(3,0,3,3)

# #售后模块
# UserList().SaleOrder(order_id,price,1,3)
