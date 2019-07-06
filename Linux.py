
import re
import threading
import time
import paramiko

# 定时任务一 放到linux系统
# def roll_back(cmd, inc = 60):
#     while True:
#         # 执行方法，函数
#         alltask()
#         time.sleep(inc)
# roll_back("echo %time%", 5)
#
# #定时任务二放到linux系统
# def roll_back(cmd, inc=60):
#     while True:
#         # 监控代码文件所在位置
#         os.system('python  /home/../monitorserver.py');
#         time.sleep(inc)
#
#
# roll_back("echo %time%", 5)
from psutil import long

"""
主方法
以下脚本可以直接在window运行
user 服务器登录用户名
host 服务器IP
password 服务器登录密码
"""
user='root'
host='192.168.153.128'
password='8496658'


def ssh_connect( _host, _username, _password ):
    try:
        _ssh_fd = paramiko.SSHClient()
        _ssh_fd.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        _ssh_fd.connect( _host, username = _username, password = _password )
    except Exception as e:
        print( 'ssh %s@%s: %s' % (_username, _host, e) )
        exit()
    return _ssh_fd
def ssh_exec_cmd( _ssh_fd, _cmd ):
    return _ssh_fd.exec_command( _cmd )

def ssh_close( _ssh_fd ):
    _ssh_fd.close()

def list1(stdout):

    b = {
    }

    for item in stdout.readlines():

        r = item
        d = r.split(":")
        a = d[1]
        a = a.strip()
        b[d[0]] = a
    return b

def list2(stdout):

    for item in stdout.readlines():
        d = item.split()
    return d

def work(host,user,password,cmd):
    sshd = ssh_connect(host, user, password)
    stdin, stdout, stderr = ssh_exec_cmd(sshd,cmd)
    err_list = stderr.readlines()
    if len(err_list) > 0:
        print('ERROR:' + err_list[0])

        exit()
    ssh_close(sshd)
    return stdout

def data(data):

    return  re.findall("(\d+)\ kB", data)[0]

"""
内存监控
"""

def mem_info():
    stdout= work(host,user,password,"cat /proc/meminfo")
    arry=list1(stdout)
    MemTotal = arry['MemTotal']
    MemFree = arry['MemFree']
    Buffers = arry['Buffers']
    Cached = arry['Cached']
    SwapCached = arry['SwapCached']
    SwapTotal = arry['SwapTotal']
    SwapFree = arry['SwapFree']
    print( '******************************内存监控*********************************')

    # print( "*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
    #
    # print("总内存：",str(float(data(MemTotal))/1024 )+' MB')
    #
    # print("空闲内存：", str(float(data(MemFree))/1024 )+' MB')
    #
    # print("给文件的缓冲大小:", str(float(data(Buffers))/1024 )+' MB')
    #
    # print("高速缓冲存储器使用的大小:", str(float(data(Cached))/1024 )+' MB')
    #
    # print("被高速缓冲存储用的交换空间大小:", str(float(data(SwapCached))/1024 )+' MB')


    if int(data(SwapTotal))== 0:
        print(u"交换内存总共为：0")

    else:

         Rate_Swap = 100 - 100 * int(data(SwapFree)) / float(data(SwapTotal))
         #print(u"交换内存利用率：", Rate_Swap)
         Free_Mem = int(data(MemFree)) + int(data(Buffers)) + int(data(Cached))
         Used_Mem = int(data(MemTotal)) - Free_Mem
         Rate_Mem = 100 * Used_Mem / float(data(MemTotal))
         a=str("%.2f" % Rate_Mem +"%")
        # print(u"内存利用率：", str("%.2f" % Rate_Mem), "%")
    return MemTotal,MemFree,a

"""
内核线程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息
"""

def vm_stat_info():
    stdout = work(host, user, password,"vmstat 1 2 | tail -n 1")
    arry = list2(stdout)
    processes_waiting=arry[0]
    processes_sleep=arry[1]
    swpd=arry[2]
    free=arry[3]
    buff=arry[4]
    cache=arry[5]
    si=arry[6]
    so=arry[7]
    io_bi=arry[8]
    io_bo=arry[9]
    system_interrupt = arry[10]
    system_context_switch=arry[11]
    cpu_user=arry[12]
    cpu_sys=arry[13]
    cpu_idle=arry[14]
    cpu_wait=arry[15]
    st=arry[16]
    print( '****************************内核线程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息监控****************************')

    print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")

    print("等待运行进程的数量:", processes_waiting)

    print("处于不间断状态的进程:", processes_sleep)

    print("使用虚拟内存(swap)的总量:", swpd)

    print("空闲的内存总量:", free)

    print("用作缓冲的内存总量:", buff)

    print("用作缓存的内存总量:", cache)

    print("交换出内存总量 :", si)

    print("交换入内存总量 :", so)

    print("从一个块设备接收:", io_bi)

    print("发送到块设备:", io_bo)

    print("每秒的中断数:", system_interrupt)

    print("每秒的上下文切换数:", system_context_switch)

    print("用户空间上进程运行的时间百分比:", cpu_user)

    print("内核空间上进程运行的时间百分比:", cpu_sys)

    print("闲置时间百分比:", cpu_idle)

    print("等待IO的时间百分比:", cpu_wait)

    print("从虚拟机偷取的时间百分比:", st)

"""
负载均衡
"""

def load_stat():

    stdout = work(host, user, password, "cat /proc/loadavg")
    arry = list2(stdout)
    loadavgs1=arry[0]
    loadavgs2=arry[1]
    loadavgs3=arry[2]
    loadavgs4=arry[3]
    loadavgs5=arry[4]
    print('************************负载均衡监控****************************')

    # print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
    #
    # print("系统1分钟前的平均负载：", loadavgs1)
    #
    # print("系统5分钟前的平均负载：", loadavgs2)
    #
    # print("系统15分钟前的平均负载：", loadavgs3)
    #
    # print("分子是正在运行的进程数,分母为总进程数：", loadavgs4)
    #
    # print("最近运行的进程id：", loadavgs5)
    return loadavgs1,loadavgs2,loadavgs3

"""
获取网络接口的输入和输出
"""

def ionetwork():
    net = {}
    stdout = work(host, user, password, "cat /proc/net/dev")
    for item in stdout.readlines():
        net_io = {}
        a= re.findall(r'\d+', item)



    print('************************获取网络接口的输入和输出监控****************************')

    print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
    eth_name = 'ens' + a[0]
    net_io['总发送流量'] = str(round(float(a[1]) / (1024.0 * 1024.0), 2))+ ' MB'
    net_io['总接收流量'] =str(round(float(a[9]) / (1024.0 * 1024.0), 2))+' MB'
    net[eth_name] = net_io
    #print(net)
    return  net_io['总发送流量'], net_io['总接收流量']



"""
磁盘空间监控
"""

def disk_stat():
    stdout = work(host, user, password, "df -h")
    for i in stdout.readlines():
        print(i)

"""
获取网络接口的输入和输出
"""


def cpu():
    stdout = work(host, user, password, 'cat /proc/stat | grep "cpu "')
    cpus=list2(stdout)
    stdout1 = work(host, user, password, 'cat /proc/stat | grep "cpu "')
    cpus1=list2(stdout1)

    print('************************cpu使用情况****************************')

    print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")

    T1 = int(cpus[1]) + int(cpus[2]) + int(cpus[3]) + int(cpus[4]) + int(cpus[5]) + int(cpus[6]) + int(cpus[8]) + int(
        cpus[9])
    T2 = int(cpus1[1]) + int(cpus1[2]) + int(cpus1[3]) + int(cpus1[4]) + int(cpus1[5]) + int(cpus1[6]) + int(
        cpus1[8]) + int(cpus1[9])
    Tol = T2 - T1
    Idle = int(cpus1[4]) - int(cpus[4])
    # print('总的cpu时间1:', T1)
    #
    # print('总的cpu时间2:', T2)
    #
    # print('时间间隔内的所有时间片:', Tol)
    #
    # print('计算空闲时间idle:', Idle)

    #print("计算cpu使用率：", 100 * (Tol - Idle) / Tol, "%")
    a=str(100 * (Tol - Idle) / Tol)+"%"
    return a






"""
第一种执行
"""

# def alltask():
#     try:
#         threads = []
#         t1 = threading.Thread(target=mem_info)
#         threads.append(t1)
#         t2 = threading.Thread(target=vm_stat_info)
#         threads.append(t2)
#         t3 = threading.Thread(target=cpu_info)
#         threads.append(t3)
#         t4 = threading.Thread(target=load_stat)
#         threads.append(t4)
#         t5 = threading.Thread(target=ionetwork)
#         threads.append(t5)
#         t6 = threading.Thread(target=disk_stat)
#         threads.append(t6)
#         t8 = threading.Thread(target=cpu)
#         threads.append(t8)
#         for n in range(len(threads)):
#             threads[n].start()
#     except Exception as e:
#         print(str(e))


"""
第二种执行
"""
if __name__ == '__main__':
    try:
        threads = []
        t1 = threading.Thread(target=mem_info)
        threads.append(t1)
        # t2 = threading.Thread(target=vm_stat_info)
        # threads.append(t2)
        t4 = threading.Thread(target=load_stat)
        threads.append(t4)
        t5 = threading.Thread(target=ionetwork)
        threads.append(t5)
        # t6 = threading.Thread(target=disk_stat)
        # threads.append(t6)
        t8 = threading.Thread(target=cpu)
        threads.append(t8)
        for n in range(len(threads)):
            threads[n].start()
    except Exception as e:
        print(str(e))



