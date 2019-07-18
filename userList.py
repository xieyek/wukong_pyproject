from login import Login
from memberinfo import member
class UserList():
    # 注册悟空掌柜，绑定邀请人
    @staticmethod
    def register_card_bill():
        token, mobile = Login().unregistered_mobile()
        member().register_shopkeeper(token)
