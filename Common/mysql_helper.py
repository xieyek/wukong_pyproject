# -*- encoding:utf-8 -*-
# 请求方式封装
import pymysql
import cf


class MysqlHelper(object):

    # def __init__(self, host="rm-m5eis3bm5xy6p7p7zno.mysql.rds.aliyuncs.com", port=3306, db="wukong_urgent",
    #              user="dengbingqiu", passwd="Dengbingqiu12#$#42", charset="utf8"):
    # def __init__(self, host="wukong-php-test.rwlb.rds.aliyuncs.com", port=3306, db="wukong_urgent",
    #              user="dengbingqiu", passwd="dengbingqiu123$@#76", charset="utf8"):
    # def __init__(self, host="rm-bp1s22133t1zn9szkio.mysql.rds.aliyuncs.com", port=3306, db="wukong_hotfix",
    #              user="hujun", passwd="HUAjun123", charset="utf8"):
    # def __init__(self, host="localhost", port=3306, db="tool",
    #              user="root", passwd="root", charset="utf8"):
    def __init__(self, host=cf.host, port=cf.port, db=cf.db, user=cf.user, passwd=cf.passwd, charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        # 建立数据库连接
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        # 获取游标
        self.cursor = self.conn.cursor()

    def close(self):
        # 关闭数据库
        self.cursor.close()
        # 断开连接
        self.conn.close()

    def all(self, sql):
        try:
            self.open()
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交sql语句
            self.conn.commit()
            # 返回结果
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)

    # 配置单个不会发送验证码的白名单
    @staticmethod
    def config_mobile(first_phone):
        sql = "UPDATE configs SET cvalue='{0}' WHERE id=92;".format(first_phone)
        MysqlHelper().all(sql)
        print("配置单个不会发送验证码的白名单")

    # 批量配置不会发送验证码的白名单
    @staticmethod
    def config_some_mobiles(first_phone=15010001000, num=10):
        phone = ""
        for i in range(num):
            phone = phone + str(first_phone + i) + ","
        sql = "UPDATE configs SET cvalue='{0}' WHERE id=92;".format(phone[:-1])
        MysqlHelper().all(sql)
        print("批量配置不会发送验证码的白名单")


