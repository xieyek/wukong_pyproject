import requests


class Login():

    codedata = {
        'phone': '18000000417',
        'sense': '8'
    }

    def __init__(self,codedata=codedata):
                 self.codedata=codedata


    def code(self):


        codeurl = "https://hotfix.shuixiongkeji.net/app/VerifyCode"
        coderes = requests.post(codeurl, data=self.codedata)
        codeno = coderes.json()['data']['content']
        return codeno


    def login(self):

        code = Login().code()
        #  code= self.code()
        url = "https://hotfix.shuixiongkeji.net/app/LoginByH5"
        data = {
            'mobile': '18000000417',
            'openid': 'eyJpdiI6InBGdkQ1N3d6TzAzclB0dDZaa2VYSXc9PSIsInZhbHVlIjoiZm54YmNIQWRoU09BV1BqMFZncnpza1MxeU9BUElVVzl2eGpLNnJWNElXcUxUTVFLallLaTJEQk52M0I4cGtiYiIsIm1hYyI6IjM4ODZhNTkxODg3MGI1MWM1NjYwYjVlNDA2ODZiMGVkYWJiNTcxZjVmN2IyZmViOTQwMWViNzJmYzJkZWFmMGEifQ==',
            'code': code
        }
        denglu = requests.post(url, data=data).json()
        if (denglu['status'] == 200):
            token = denglu['data']['token']
            return str(token)
        else:
            print('token获取失败:' + denglu )




# Login().code()
#Login().login()
