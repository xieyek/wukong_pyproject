import random
import requests
import cf
from Common.common import  Common
from http_method import Http
# from memberinfo import member
from memberinfo import member


class Login():
    # 掌柜登录注册获取验证码
    @staticmethod
    def post_verify_code(phone, sense="8"):
        data = {
            "phone": phone,
            "sense": sense,  # 8登录注册
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "app/VerifyCode", data1, None)
        print("掌柜登录获取验证码" + str(obj.status_code))
        Common.out_error(obj)
        return obj
    # 掌柜登录H5  13617518030 13965681892
    @staticmethod
    def login(mobile=cf.recommend_mobile):
        code = Login().post_verify_code(mobile, "8")
        code_content = Common.loads_text(code)["data"]["content"]
        # code_content = ShopKeeper.get_code(mobile)
        data = {
            "mobile": mobile,
            "code": code_content,
            "openid": cf.openid
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "app/LoginByH5", data1, None)
        print("掌柜登录H5" + str(obj.status_code))
        Common.out_error(obj)
        return obj
    # 掌柜登录获取token
    @staticmethod
    def login_token(mobile=cf.recommend_mobile):
        # MysqlHelper().config_mobile(mobile)
        m = Login().login(mobile)
        if Common.loads_text(m)["message"] == "success":
            token = "Bearer " + Common.loads_text(m)["data"]["token"]
            return token
        else:
            print(mobile, m.json())
            Common.strike_n(65)
            token = Login().login_token(mobile)
            return token
    # 返回一个未注册的手机的token
    @staticmethod
    def unregistered_mobile():
        # 随机获取手机号
        num = random.randint(1, 99999999)
        mobile = str(19900000000 + num)
        print(mobile)
        # 获取token
        token = Login.login_token(mobile)
        # 获取个人信息
        f = member().post_update_info(token, cf.recommend_mobile)
        if Common.loads_text(f)["message"] == "该用户不存在，请注册":
            return token, mobile
        else:
            Common.strike()
            Login.unregistered_mobile()

# Login().code()
#Login().login()
