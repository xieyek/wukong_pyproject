import datetime
import time
from apscheduler.triggers.interval import IntervalTrigger
from Linux import *
from apscheduler.schedulers.blocking import BlockingScheduler
class Clock(object):
   ls=[1,2,3,4,5]
   time_out = 1
   @staticmethod
   def my_job():
      print('hello world')
   # 定时任务，on_off开关，time_out秒数，func函数
   @staticmethod
   def work_timer(time_out, func):
        scheduler = BlockingScheduler()
        trigger = IntervalTrigger(seconds=time_out)
        scheduler.add_job(func, trigger)
        scheduler.start()
   #日期定时器
   @staticmethod
   def cur_timer(start_date,hours,minutes,func):
          scheduler=BlockingScheduler()
          trigger = IntervalTrigger(start_date=start_date,hours=hours,minutes=minutes)  #start_date='2019-6-17',hours=16,minutes=2
          scheduler.add_job(func,trigger)
          scheduler.start()
   # 休眠多久执行函数
   @staticmethod
   def Time_out(secs, function):
        time.sleep(secs)
        function()

   @staticmethod
   def bianli(list, func):
       for i in list:
           func()


Clock.bianli(ls,)
