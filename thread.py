# 多线程测试脚本，支持并发
from memberinfo import member
from order import order
from login import Login
import threading
from datetime import *
import time
from  order import order
from memberinfo import member
from cf import *
from showping import showping
from  order import order
from login import Login
from business import Business
from Common.common import Common
import json
membertoken=shopkeeper_token
businesstoken=supplier_token
admin_token=operation_token

Thread_total_num = 2  # 总进程
OneThread_num = 2  # 每个进程的并发数即是子进程
sun_time = 0  #初始化变量用来统计响应时间
succes_total = 0  #初始化变量用来统计并发成功数
#token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaG90Zml4LnNodWl4aW9uZ2tlamkubmV0XC9hcHBcL0RhaWx5U2FsZVVucGFpZE9yZGVyIiwiaWF0IjoxNTU5MTM2MDk1LCJleHAiOjE1NTkxNDEzNjcsIm5iZiI6MTU1OTE0MDc2NywianRpIjoiVnZPUlRram84NFJsVkZ5WSIsInN1YiI6NDUzMDIsInBydiI6IjZkOWJkZjNhOTA1NzZhN2E2MmY4Y2M1ZDJjNWJiNmY4ZWFjYWQ4MTciLCJpZCI6NDUzMDIsInJvbGUiOiJVU0VSIiwiaXNfdXNlciI6dHJ1ZSwicm9sZV9pZCI6MCwicmVzZXRfdGltZSI6IjIwMTktMDUtMjkgMjE6MjA6MzQiLCJvcGVuaWQiOiJvSEZYSTFBeDJ1UEtZYVhZdWpKNmlCVHh6VVJzIiwidGhpcmRfcGFydF9pZCI6MTM1OTI0fQ.w7349z2AOPB0Iwx7KTIHTX59cYxh7j5hXumGJs_tLmE'
#token=Login().login() # 可以直接调用函数获取token menber=member()
# memberinfo=member.userinfo(token) #用户信息
order = order()

def work():  # 该函数支持添加单接口或者多接口
    start_time = time.time() #线程开启时间
    # 以下填写需要的接口

    bulidorder = order.bulidorder(membertoken)  # 创建订单
    trade_no = bulidorder[0]
    short_no = bulidorder[1]
    pyorder = order.payorder(membertoken, trade_no)  # 余额购买


    # 以上填写需要的接口
    end_time = time.time()
    res_time = end_time-start_time  #线程结束时间
    print('单线程响应时间：' + str(res_time))  # 打印进程响应时间
    return  res_time


def working():  # 线程测试函数
    global sun_time
    global succes_total
    global OneThread_num
    for i in range(0, OneThread_num):
        sun_time = work()
        sun_time += sun_time
        succes_total += 1
def run():  # 多线程函数
    global Thread_total_num
    global leiji_num
    Threads = []
    try:
        for i in range(0, Thread_total_num):
            t = threading.Thread(target=working(), name='T' + str(i))
            t.setDaemon(True)
            Threads.append(t)
        for t in Threads:
            t.start()
        for t in Threads:
            t.join()  # 阻塞函数，单位：秒，即时等待子线程多久主线程才开始跑，超过时间不管子线程完不完成主线程都会跑，默认空
    except Exception as e:
        print(e)
if __name__ == "__main__":
    run()
    print('线程并发数：' + str(Thread_total_num * OneThread_num))
    print('并发成功数：' + str(succes_total))
    print('并发成功率：' + str(succes_total / (Thread_total_num * OneThread_num) * 100) + "%")
    print('并发总时间：'+str(sun_time))
    print('平均响应时间：' + str(sun_time / succes_total))
    print('tps：' + str((succes_total) / (sun_time / succes_total)))
    print('end')
