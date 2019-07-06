# -*- coding:utf-8 -*-
# 公共方法
import base64
import datetime
import json
import random
import time
import requests
import cf
from Common import var
from Common.http_method import Http


class Common(object):

    # 返回需要环境
    @staticmethod
    def first_url(n=cf.first_url):
        url_list = [
            "http://urgent.shuixiongkeji.net/",
            "http://big.shuixiongkeji.net/",
            "http://h5.shuixiongkeji.net/",
            "http://finance.shuixiongkeji.net/",
            "http://spare.shuixiongkeji.net/",
            "http://adminv1.shuixiongkeji.net/",
            "http://reserve.shuixiongkeji.net/",
            "http://hotfix.shuixiongkeji.net"
        ]
        # print(url_list[n])
        return url_list[n]

    # 暂停5秒
    @staticmethod
    def strike():
        time.sleep(5)

    # 暂停2秒
    @staticmethod
    def strike_2():
        time.sleep(2)

    # 暂停n秒
    @staticmethod
    def strike_n(n=10):
        time.sleep(n)

    # 通过一个值找另一个键对应的值
    @staticmethod
    def find_element(list1, element_type, key="Id"):
        for i in list1:
            if element_type in i.values():
                obj = i[key]
                return obj

    # 如果接口请求失败,报错提示
    @staticmethod
    def out_error(o):
        pass
        # if o.status_code != 200 or o.json()["status"] != 200:
        #     print('请求失败' + str(o.status_code) + o.url)
        #     print(o.json())
        #     raise NameError(o.json())

    # 上传图片
    @staticmethod
    def photo(org_url, photoname="mn"):
        p = open(var.media_path + '{0}.jpg'.format(photoname), 'rb')
        pp = p.read()
        p.close()
        # h = {'Content-Type': ''}
        Http.put(org_url, pp, None)

    # 上传base64位的图片
    @staticmethod
    def photo_base64(photoname="mn"):
        p = open(var.media_path + '{0}.jpg'.format(photoname), 'rb')
        pp = p.read()
        base64_data = base64.b64encode(pp)
        base64_data1 = bytes.decode(base64_data)
        return base64_data1

    # 上传视频
    @staticmethod
    def video(org_url, videoname):
        p = open(var.media_path + '{0}.jpg'.format(videoname), 'rb')
        pp = p.read()
        p.close()
        # h = {'Content-Type': ''}
        Http.put(org_url, pp, None)

    # 将dict类型的数据转成str
    @staticmethod
    def dumps_text(data):
        obj = json.dumps(data)
        return obj

    # 将str类型的数据转成dict
    @staticmethod
    def loads_text(data):
        obj = json.loads(data.text)
        return obj

    # 将两个List拼成dict
    @staticmethod
    def dict_text(data1,data2):
        obj=dict(zip(data1,data2))
        return obj


    # 获取当前时间
    @staticmethod
    def current_time(pt=0):
        t = round(time.time()+pt)
        timeArray = time.localtime(t)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return now_time

    # 获取当前时间戳
    @staticmethod
    def current_time_stamp():
        t = round(time.time())
        t = str(t)
        # print(t)
        return t

    @staticmethod
    def case_clear():
        pass

    # 重试
    @staticmethod
    def retry(checkCallResult, call, *param, attempt_num=5, wait_sec=2, result_type=1, data_location=None):
        i = 0
        # 针对列表数据验证
        if result_type == 1:
            while i < attempt_num:
                result = call(*param)
                length = len(Common.loads_text(result)["value"])
                if length == checkCallResult:
                    return result
                else:
                    i += 1
                    time.sleep(wait_sec)
                print(i)
                if i == attempt_num:
                    raise NameError("找不到指定结果,实际结果为：%d" % length)
        # 针对群数据验证
        elif result_type == 2:
            while i < attempt_num:
                result = call(*param)
                length = len(result)
                if length == checkCallResult:
                    return result
                else:
                    i += 1
                    time.sleep(wait_sec)
                print(i)
                if i == attempt_num:
                    raise NameError("找不到指定结果,实际结果为：%d" % length)
        # 针对某个数据验证
        elif result_type == 3:
            while i < attempt_num:
                r = call(*param)
                result = Common.loads_text(r)
                for k in data_location:
                    result = result[k]
                if result == checkCallResult:
                    return result
                else:
                    i += 1
                    time.sleep(wait_sec)
                print(i)
                if i == attempt_num:
                    raise NameError("找不到指定结果,实际结果为：%d" % result)
        # 针对某个数据验证
        else:
            while i < attempt_num:
                result = call(*param)
                for k in result_type:
                    result = result[k]
                if result == checkCallResult:
                    return result
                else:
                    i += 1
                    time.sleep(wait_sec)
                print(i)
                if i == attempt_num:
                    raise NameError("找不到指定结果,实际结果为：%d" % result)

    # 刷新redis缓存接口
    @staticmethod
    def options_FlushCache():
        requests.options("http://urgent.shuixiongkeji.net/app/FlushCache")

    # 获取验证码
    @staticmethod
    def sms_content(phone, sense):
        data = {
            "phone": phone,
            "sense": sense  # 12供应商忘记密码重置密码,4供应商更改登录账号,6重置安全密码
        }
        data1 = Common.dumps_text(data)
        obj = Http.post(Common.first_url() + "Sms", data1, None)
        print("获取验证码" + str(obj.status_code))
        Common.out_error(obj)
        return Common.loads_text(obj)["data"][0]["attributes"]["content"]
    @staticmethod
    def random_num(num):  # 返回指定位数的随机数字字符串
        id = ''.join(str(i) for i in random.sample(range(0, 9), num))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
        return id
    @staticmethod
    def read_isspace(dir):  # 有空格的文本处理，返回逗号分隔的数组
        file = open(dir, 'r')
        # 按行读取
        contents = file.readlines()
        # 数组
        arr = []
        for item in contents:
            # 清除换行、空格
            content = item.strip()
            p = ','.join(content.split())
            temp = p.split(",")
            arr.append(temp)
        return arr
    @staticmethod
    def read_douhao(dir):  # 有逗号的文本处理，重新组成数组
        file = open(dir, 'r')
        # 按行读取
        contents = file.readlines()
        # 数组
        arr = []
        for item in contents:
            # 清除换行、空格
            content = item.strip()
            temp = content.split(",")
            arr.append(temp)
        return arr
