import socket
import pymysql
import time
# import pandas as pd
import array

# sql = 'SELECT * FROM daily_sale_orders WHERE id=1;'
class Mysql():

    # sql服务端配置
    def serverdatabass(self):

        server = socket.socket()
        server.bind('wukong-php-test.rwlb.rds.aliyuncs.com', 3306)
        server.listen(100)
        while True:
            conn, addr = server.accept()
            conn.send("服务器信息".encode())
            print(conn.recv(1024))
        conn.close()
    #客户端连接
    def sql_connetion(self,host,user,pwd,db_name):
        conn = pymysql.connect(host, user, pwd, db_name)
        return conn

    # 客户端执行sql语句
    def sqlclien(self,sql):
        #big
        #conn=self.sql_connetion('rm-bp15vz0kbspktrxh7vo.mysql.rds.aliyuncs.com', 'wukong_test', "wukong_test_122", "wukong_big")
        #H5
        conn = Mysql().sql_connetion('wukong-php-test.rwlb.rds.aliyuncs.com', 'xieye', "xieye#*&_1237", "wukong_big")
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            results = cur.fetchall()
        except:
            conn.rollback()
            conn.close()
            cur.close()
        return results




