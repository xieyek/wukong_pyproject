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
        conn=self.sql_connetion('wukong-php-test.rwlb.rds.aliyuncs.com', 'xieye', "xieye#*&_1237", "wukong_exploit")
       # conn = pymysql.connect('wukong-php-test.rwlb.rds.aliyuncs.com', 'xieye', "xieye#*&_1237", "wukong_hotfix")
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

    # def execude_sql(self,sql):
    #     # 创建连接
    #     try:
    #         conn = self.sql_connetion('wukong-php-test.rwlb.rds.aliyuncs.com', 'xieye', "xieye#*&_1237",
    #                                   "wukong_exploit")
    #     except:
    #         print('数据库连接失败，10s后重试')
    #         time.sleep(10)
    #     # 创建游标
    #     cursor = conn.cursor()
    #     cursor.execute(sql)
    #     data = cursor.fetchall()
    #     # cols为字段信息 例如(('factory_id', 253, None, 6, 6, 0, False), ('szDeviceId', 253, None, 30, 30, 0, False),('update_time', 7, None, 19, 19, 0, False))
    #     cols = cursor.description
    #     # 执行
    #     conn.commit()
    #     conn.close()
    #     # 将数据truple转换为DataFrame
    #     col = []
    #     for i in cols:
    #         col.append(i[0])
    #     data = list(map(list, data))
    #     data = pd.DataFrame(data, columns=col)
    #     print(data)
    #     return data




